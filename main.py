import datetime
import psycopg2
import sys
import Utils
from Views.main_window import QtWidgets, Ui_MainWindow
from Views.login_form import Ui_LoginForm
from Views.sign_up_form import Ui_Sign_up_form
from Views.markets_pages_window import Ui_M_Pages
from Views.review_pages import Ui_market_pages_window2
from Views.login_failed_dialog import Ui_login_failed_dialog
from Views.review_window import Ui_review_window
from Views.search_window import Ui_SearchWindow
from Views.widget_pop_up import Ui_widget_pop_up
from Views.delete_pop_up import Ui_pop_up_delete

conn = psycopg2.connect(dbname='farmers_markets',
                        host='localhost',
                        user='marketsuser',
                        password='Pa$$W0rd',
                        port='5432')


def do_delete():
    m_name = m_page_ui.lMPages.currentItem().text().split(',')[0][6:]
    cursor = conn.cursor()
    cursor.execute("""DELETE 
                      FROM markets
                      WHERE market_name = %(name)s;""", {'name': m_name})
    conn.commit()
    Del_pop_up.close()
    m_page_ui.lMPages.clear()


def delete_selected():
    item = m_page_ui.lMPages.currentItem().text().split(',')[0][6:]
    del_pop_ui.lblDelete.setText(f'Delete this record for {item}?')
    Del_pop_up.show()
    del_pop_ui.btnN.clicked.connect(Del_pop_up.close)
    del_pop_ui.btnY.clicked.connect(do_delete)


def populate_cbm_pages(arr):
    combo_items = []
    counter = -1
    for _i in arr:
        counter += 1
        combo_items.append(str(counter))
    m_page_ui.cbMPages.addItems(combo_items)


def populate_cbm_select():
    data = Utils.do_select()
    combo_items = []
    for i in data:
        combo_items.append(i[1])
    review_ui.cbMarketSelect.addItems(combo_items)


def populate_cbm_scores():
    combo_items = ['1', '2', '3', '4', '5']
    review_ui.cbScores.addItems(combo_items)


def populate_cbm_reviews():
    combo_items = get_users_list()
    u_review_ui.cmDReviews.addItems(combo_items)


def sign_up():
    f_name = sign_up_ui.lnFname.text()
    l_name = sign_up_ui.lnLname.text()
    usr_name = sign_up_ui.lnUsername.text()
    pswd = sign_up_ui.lnPassword.text()

    cursor = conn.cursor()
    cursor.execute("""INSERT 
                            INTO users (fname, lname, username, password_hash)
                            VALUES (%s, %s, %s, %s);""", (f_name, l_name, usr_name, pswd))
    conn.commit()


def log_in():
    usr_name = login_ui.lnUsername.text()
    pswd = login_ui.lnPassword.text()

    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM users 
                            WHERE username = %(usr_name)s AND password_hash = %(pswd)s;""",
                   {"usr_name": usr_name, "pswd": pswd})

    res = cursor.fetchall()
    if Utils.validate_signing(res):
        Utils.log_user(str(res[0]).strip("()"))
        Login_Form.close()
        MainWindow.show()
    else:
        Login_failed_dialog.show()


def get_review_data():
    cursor = conn.cursor()
    with open('user_log.txt', 'r') as file:
        usr_data = file.read().strip("()").replace("'", '')
    usr_id = usr_data[0]
    m_name = review_ui.cbMarketSelect.currentText()
    cursor.execute("""SELECT market_id FROM markets
                            WHERE market_name = %(m_name)s;""", {"m_name": m_name})
    m_id = str(cursor.fetchall()[0]).strip("()").replace(',', '')
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    score = review_ui.cbScores.currentText()
    txt = review_ui.tReviewBody.toPlainText()
    return usr_id, m_id, date, score, txt


def review_market():
    usr_id, m_id, date, score, txt = get_review_data()
    cursor = conn.cursor()
    cursor.execute("""INSERT 
                            INTO reviews (user_id, market_id, date_time, score, review)
                            VALUES (%s, %s, %s, %s, %s);""", (usr_id, m_id, date, score, txt))
    conn.commit()


def get_users_list():
    cursor = conn.cursor()
    cursor.execute("""SELECT username FROM users;""")
    raw = cursor.fetchall()
    res = []
    for i in range(len(raw)):
        res.append(raw[i][0])
    return res


def display_reviews():
    u_review_ui.tMPages.insertPlainText("")
    cursor = conn.cursor()
    usr_name = u_review_ui.cmDReviews.currentText()
    cursor.execute("""SELECT username, reviews.date_time, reviews.score, reviews.review, markets.market_name
                      FROM users 
                      LEFT JOIN reviews ON users.user_id = reviews.user_id
                      LEFT JOIN markets ON markets.market_id = reviews.market_id
                      WHERE username = %(user_name)s; """, {'user_name': usr_name})
    raw = cursor.fetchall()

    res_dict = {}

    for i in raw:
        key = i[0]
        res_dict.setdefault(key, []).append({
            'Date': i[1],
            'Market name': i[4],
            'Score': i[2],
            'Review': i[3]
        })

    res = ''
    u_review_ui.tMPages.clear()
    for i in range(len(res_dict[usr_name])):
        if all(value is None for value in res_dict[usr_name][0].values()):
            res = "No reviews by this user found"
        else:
            res += 'Date: ' + str(res_dict[usr_name][i]['Date']) + '\n'
            res += 'Market name : ' + str(res_dict[usr_name][i]['Market name']) + '\n'
            res += 'Score : ' + str(res_dict[usr_name][i]['Score']) + '\n'
            res += 'Review: ' + str(res_dict[usr_name][i]['Review']) + ('\n' * 3)
    u_review_ui.tMPages.insertPlainText(res)


def show_detailed_info(item):
    item = item.text().split(',')[0][6:]
    pop_up_ui.tPop.setText(Utils.format_full_data(Utils.do_select_full_data(item)[0]))
    Pop_up.show()


def search():
    search_ui.lSearch.clear()
    if search_ui.lnCity.text():
        search_param = search_ui.lnCity.text()
        for i in Utils.do_select_by_city(search_param):
            search_ui.lSearch.addItem(Utils.format_search(i))
    elif search_ui.lnState.text():
        search_param = search_ui.lnState.text()
        for i in Utils.do_select_by_state(search_param):
            search_ui.lSearch.addItem(Utils.format_search(i))
    elif search_ui.lnZip.text():
        search_param = search_ui.lnZip.text()
        try:
            int(search_param)
            for i in Utils.do_select_by_zip(search_param):
                search_ui.lSearch.addItem(Utils.format_search(i))
        except ValueError:
            pass
    elif search_ui.lnCoords.text():
        find_closest()
    if search_ui.lSearch.count() == 0:
        pop_up_ui.tPop.setText('No data available for the specified criteria')
        Pop_up.show()
    search_ui.lnState.clear()
    search_ui.lnCity.clear()
    search_ui.lnZip.clear()
    search_ui.lnCoords.clear()


def toggle_coords_search():
    if search_ui.cbxCoords.isChecked():
        search_ui.cbxCoords.stateChanged.connect(search_ui.lblLimit.show)
        search_ui.cbxCoords.stateChanged.connect(search_ui.cbxMyCoords.show)
        search_ui.cbxCoords.stateChanged.connect(search_ui.lnCoords.show)


    else:
        search_ui.cbxCoords.stateChanged.connect(search_ui.lblLimit.hide)
        search_ui.cbxCoords.stateChanged.connect(search_ui.cbxMyCoords.hide)
        search_ui.cbxCoords.stateChanged.connect(search_ui.lnCoords.hide)


def get_coords():
    return [float(i) for i in (search_ui.lnCoords.text().split(', '))]


def fill_my_coords():
    if search_ui.cbxMyCoords.isChecked():
        coords = str(Utils.get_my_coords()).strip('[]')
        search_ui.lnCoords.setText(coords)
    else:
        search_ui.lnCoords.setText('')
        search_ui.lSearch.clear()


def find_closest():
    limit = int(search_ui.sbLimit.text())
    try:
        my_loc = [eval(i) for i in search_ui.lnCoords.text().split(', ')]
        data = Utils.do_select()
        temp_list = []
        res_list = []
        for i in data:
            if i[-1] and i[-2]:
                temp_list.append([i[1], i[-2:]])
        if limit > 0:
            for i in range(len(temp_list)):
                if Utils.calc_distance(temp_list[i][1], my_loc) <= limit:
                    res_list.append((Utils.calc_distance(temp_list[i][1], my_loc), temp_list[i][0]))
        else:
            for i in range(len(temp_list)):
                res_list.append((Utils.calc_distance(temp_list[i][1], my_loc), temp_list[i][0]))
        try:
            res_list = sorted(res_list)[1:6]
        except IndexError:
            res_list = sorted(res_list)[1:]

        if res_list:
            for i in res_list:
                search_ui.lSearch.addItem(Utils.format_closest(i))

            else:
                pop_up_ui.tPop.setText('No data available for the specified range criteria')
    except NameError:
        pass
    except IndexError:
        pass

def fetch_markets_page_default():
    m_page_ui.lMPages.clear()
    arr = Utils.fetch_all_markets()
    idx = m_page_ui.cbMPages.currentText()
    m_page_ui.lMPages.addItems(arr[int(idx)])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    Login_Form = QtWidgets.QWidget()
    Sign_Up_Form = QtWidgets.QWidget()
    Markets_Pages = QtWidgets.QMainWindow()
    Login_failed_dialog = QtWidgets.QWidget()
    Review_window = QtWidgets.QMainWindow()
    User_Reviews_Window = QtWidgets.QMainWindow()
    Search_Window = QtWidgets.QMainWindow()
    Pop_up = QtWidgets.QWidget()
    Del_pop_up = QtWidgets.QWidget()

    ui = Ui_MainWindow()
    login_ui = Ui_LoginForm()
    sign_up_ui = Ui_Sign_up_form()
    m_page_ui = Ui_M_Pages()
    log_fail_ui = Ui_login_failed_dialog()
    review_ui = Ui_review_window()
    u_review_ui = Ui_market_pages_window2()
    search_ui = Ui_SearchWindow()
    pop_up_ui = Ui_widget_pop_up()
    del_pop_ui = Ui_pop_up_delete()

    ui.setupUi(MainWindow)
    sign_up_ui.setupUi(Sign_Up_Form)
    login_ui.setupUi(Login_Form)
    m_page_ui.setupUi(Markets_Pages)
    log_fail_ui.setupUi(Login_failed_dialog)
    review_ui.setupUi(Review_window)
    u_review_ui.setupUi(User_Reviews_Window)
    search_ui.setupUi(Search_Window)
    pop_up_ui.setupUi(Pop_up)
    del_pop_ui.setupUi(Del_pop_up)

    Login_Form.show()

    login_ui.btnSignUp.clicked.connect(Sign_Up_Form.show)
    login_ui.btnLogin.clicked.connect(log_in)

    log_fail_ui.btnRetry.clicked.connect(Login_failed_dialog.close)
    log_fail_ui.btnCancel.clicked.connect(app.quit)

    sign_up_ui.btnCancel.clicked.connect(app.quit)
    sign_up_ui.btnSignUp.clicked.connect(sign_up)
    sign_up_ui.btnSignUp.clicked.connect(Sign_Up_Form.close)

    ui.btnMarketsPage.clicked.connect(Markets_Pages.show)
    ui.btnLeaveReview.clicked.connect(Review_window.show)
    ui.btnUsrReviews.clicked.connect(User_Reviews_Window.show)
    ui.btnSearch.clicked.connect(Search_Window.show)

    m_page_ui.cbMPages.addItem(populate_cbm_pages(Utils.fetch_all_markets()))
    m_page_ui.cbMPages.activated.connect(fetch_markets_page_default)
    m_page_ui.lMPages.itemDoubleClicked.connect(show_detailed_info)

    m_page_ui.btnDelete.clicked.connect(delete_selected)

    review_ui.cbMarketSelect.addItem(populate_cbm_select())
    review_ui.cbScores.addItem(populate_cbm_scores())
    review_ui.btnReview.clicked.connect(review_market)
    review_ui.btnReview.clicked.connect(Review_window.close)

    u_review_ui.cmDReviews.addItem(populate_cbm_reviews())
    u_review_ui.cmDReviews.activated.connect(display_reviews)

    search_ui.lnCoords.hide()
    search_ui.lblLimit.hide()
    search_ui.cbxMyCoords.hide()
    search_ui.cbxCoords.toggled.connect(toggle_coords_search)
    search_ui.cbxMyCoords.toggled.connect(fill_my_coords)
    search_ui.btnSearch.clicked.connect(search)
    search_ui.lSearch.itemDoubleClicked.connect(show_detailed_info)

    pop_up_ui.btnPop.clicked.connect(Pop_up.close)

    sys.exit(app.exec())
