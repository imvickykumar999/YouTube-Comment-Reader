
import os
from flask import Flask, flash, request, redirect, render_template, send_from_directory
from werkzeug.utils import secure_filename
from vicks.encrypt import encryptpdf as enc

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/<filename>')
def send_image(filename):
    return send_from_directory("", filename)

# return redirect(f'/{loc}')

@app.route("/")
def report():
    return render_template('form.html')

@app.route('/converted_report', methods=['POST', 'GET'])
def converted_report():

    ld_itemqty = request.form['ld_itemqty']
    ld_itemunit = request.form['ld_itemunit']
    ld_itemprice = request.form['ld_itemprice']
    ld_item = request.form['ld_item']
    ld_purchasedate = request.form['ld_purchasedate']
    ld_paymentmode = request.form['ld_paymentmode']
    ld_paymentdate = request.form['ld_paymentdate']
    ld_date1 = request.form['ld_date1']
    ld_amountpaid = request.form['ld_amountpaid']
    ld_itemqtydelivered = request.form['ld_itemqtydelivered']
    ld_legalnoticedate = request.form['ld_legalnoticedate']
    ld_legalnoticedelivereddate = request.form['ld_legalnoticedelivereddate']
    ld_suitvaluation = request.form['ld_suitvaluation']
    ld_courtfees = request.form['ld_courtfees']
    ld_returnamount = request.form['ld_returnamount']


    text = f'''
                                                In the court of HC
                                            overpaid Case Number 123
                                        Suit for recovery of money OverPaid


    (1) That the plaintiff purchased {ld_item} @ Rs. {ld_itemprice} per {ld_item} from the
    defendant on date {ld_purchasedate}

    (2) That sum of Rs {ld_amountpaid} was paid to the defendant
    through {ld_paymentmode} on {ld_paymentdate}

    (3) That on receipt of {ld_item} on {ld_date1} without verifying the
    quantity of goods plaintiff paid the whole amount of
    Rs. {ld_amountpaid} to the defendant.

    (4) That on verifying the quantity of goods , it was found that
    only {ld_itemqtydelivered} were sent by the defendant whereas
    he has to deliver {ld_itemqty} Ignorant of short supply plaintiff
    paid the whole amount.

    (5) That the plaintiff repeatedly requested the defendant to
    return Rs. {ld_returnamount} which was
    wrongly overpaid but no satisfactory reply given till date.

    (6) That the plaintiff sent a legal notice dated {ld_legalnoticedate}
    through his counsel to the defendant for paying Rs. {ld_returnamount}
    and the same was delivered to him on {ld_legalnoticedelivereddate}

    (7) That it is very surprising that the defendant neither paid
    the amount demanded nor replied to the legal notice sent by
    the plaintiff.

    (8) That in the aforesaid facts and circumstances, the plaintiff
    has no option expect approaching to this court for resolving
    his genuine grievance.

    (9) That the cause of action arose on the date when plaintiff
    requested the defendant to return the þÿoverpaid money,
    but defendant didn t returned the money overpaid.

    (10) That the valuation of the suit for the purpose of
    jurisdiction is Rs. {ld_courtfees}

    (11) That this court has territorial and pecuniary jurisdiction
    to hear and decide this case

    (12) That the suit is within limitation

    (13) That it is humbly prayed that the court shall a pass a decree
    in favour of plaintiff for the sum of Rs. {ld_returnamount}
    along with interest & cost and any other relief in the favour
    of plaintiff which this court deems fit in the facts and
    circumstances of the case

    Date : 26/04/2021

    Verification

    1. That I (above named petitioner) do solemnly affirmed and verify
    the aforesaid contents stated in above para are correct and
    true to the best of my knowledge and belief.

    2. That as per my knowledge and belief nothing has been concealed.

    Date : 26/04/2021

    '''

    with open("myfile.txt", "w") as f:
        f.write(text)

    from vicks import text2pdf as pdf
    pdf.convert()

    return render_template('form.html',

    ld_itemqty = ld_itemqty,
    ld_itemunit = ld_itemunit,
    ld_item = ld_item,
    ld_itemprice = ld_itemprice,
    ld_purchasedate = ld_purchasedate,
    ld_paymentmode = ld_paymentmode,
    ld_paymentdate = ld_paymentdate,
    ld_date1 = ld_date1,
    ld_amountpaid = ld_amountpaid,
    ld_itemqtydelivered = ld_itemqtydelivered,
    ld_legalnoticedate = ld_legalnoticedate,
    ld_legalnoticedelivereddate = ld_legalnoticedelivereddate,
    ld_suitvaluation = ld_suitvaluation,
    ld_courtfees = ld_courtfees,
    ld_returnamount = ld_returnamount
                           )

if __name__ == '__main__':
    app.run(debug=True)
