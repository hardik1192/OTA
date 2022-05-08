from flask import Flask, render_template, request, url_for , flash,redirect
import pandas as pd
import math
app = Flask(__name__)
app.secret_key = "asdfghjkl"


df = pd.read_csv("crc_length.csv")
df['Ver'] = df['Ver'].astype('str')
df.to_string()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/jennic',methods=["GET","POST"])
def receive_data_jennic():

    if request.method == "POST":
        if (request.form.get("jen-ver") == "Nothing") or (request.form.get("jen-chip") == "Nothing"):
            flash('Please select valid version')
            return redirect(url_for('home'))
            # return "<h1>Please select valid version</h1>"
        else:
            jennic_name = request.form.get("jen-ver",False)
            jennic_chip = request.form.get("jen-chip", False)
            crc = df.loc[(df['Ver'] == jennic_name) & (df['Chiptype'] == jennic_chip), 'CRC']
            length = df.loc[(df['Ver'] == jennic_name) & (df['Chiptype'] == jennic_chip), 'Length']
            crc_string = (crc.to_string(index=False))
            length_string = (length.to_string(index=False))
            jennic_float = float(jennic_name)
            jennic_name_num = math.trunc(jennic_float)
            return render_template("jennic.html",j_name=jennic_name_num,j_chip=jennic_chip,crc_name = crc_string,length_name=length_string)

@app.route('/efm',methods=["GET","POST"])
def receive_data_efm():
    if request.method == "POST":
        if (request.form.get("ef-ver") == "Nothing") or (request.form.get("efm-chip") == "Nothing"):
            flash('Please select valid version')
            return redirect(url_for('home'))
            # return "<h1>Please select valid version</h1>"
        else:
            efm_name = request.form.get("ef-ver",False)
            e_chip_e = request.form.get("efm-chip", False)
            crc = df.loc[(df['Ver'] == efm_name) & (df['Chiptype'] == e_chip_e) , 'CRC']
            length = df.loc[(df['Ver'] == efm_name) & (df['Chiptype'] == e_chip_e) , 'Length']
            crc_string = (crc.to_string(index=False))
            length_string = (length.to_string(index=False))
            efm_float = float(efm_name)
            efm_name_num = math.trunc(efm_float)
            return render_template("efm.html",e_name=efm_name_num,e_chip=e_chip_e,cr_name=crc_string,le_name=length_string)

@app.route('/jennic-NDE',methods=["GET","POST"])
def receive_data_jennic_NDE():
    if request.method == "POST":
        if (request.form.get("jen-ver") == "Nothing") or (request.form.get("jen-chip") == "Nothing"):
            flash('Please select valid version')
            return redirect(url_for('home'))
        elif int(len(request.form.get("mac", False))) < 16:
            flash('Minimum 16 digit required for MAC address', category="Error")
            return redirect(url_for('home'))
        else:
            mac_addr = request.form.get("mac",False)
            jennic_name = request.form.get("jen-ver",False)
            jennic_chip = request.form.get("jen-chip", False)
            crc = df.loc[(df['Ver'] == jennic_name) & (df['Chiptype'] == jennic_chip), 'CRC']
            length = df.loc[(df['Ver'] == jennic_name) & (df['Chiptype'] == jennic_chip), 'Length']
            crc_string = (crc.to_string(index=False))
            length_string = (length.to_string(index=False))
            jennic_float = float(jennic_name)
            jennic_name_num = math.trunc(jennic_float)
            return render_template("jennic_node.html",node_mac=mac_addr,j_name=jennic_name_num,j_chip=jennic_chip,crc_name = crc_string,length_name=length_string)

@app.route('/efm-nde',methods=["GET","POST"])
def receive_data_efm_NDE():
    if request.method == "POST":
        if (request.form.get("ef-ver") == "Nothing") or (request.form.get("efm-chip") == "Nothing"):
            flash('Please select valid version')
            return redirect(url_for('home'))
        elif int(len(request.form.get("mac", False))) < 16:
            flash('Minimum 16 digit required for MAC address', category="Error")
            return redirect(url_for('home'))
        else:
            mac_addr = request.form.get("mac", False)
            efm_name = request.form.get("ef-ver",False)
            e_chip_e = request.form.get("efm-chip", False)
            crc = df.loc[(df['Ver'] == efm_name) & (df['Chiptype'] == e_chip_e) , 'CRC']
            length = df.loc[(df['Ver'] == efm_name) & (df['Chiptype'] == e_chip_e) , 'Length']
            crc_string = (crc.to_string(index=False))
            length_string = (length.to_string(index=False))
            efm_float = float(efm_name)
            efm_name_num = math.trunc(efm_float)
            return render_template("efm_node.html",node_mac=mac_addr,e_name=efm_name_num,e_chip=e_chip_e,cr_name=crc_string,le_name=length_string)

@app.route('/jennic-NDE-direct',methods=["GET","POST"])
def receive_data_jennic_direct_NDE():
    if request.method == "POST":
        if (request.form.get("jen-ver") == "Nothing") or (request.form.get("jen-chip") == "Nothing"):
            flash('Please select valid version')
            return redirect(url_for('home'))
        elif int(len(request.form.get("mac", False))) < 16:
            flash('Minimum 16 digit required for MAC address', category="Error")
            return redirect(url_for('home'))
        else:
            mac_addr = request.form.get("mac",False)
            jennic_name = request.form.get("jen-ver",False)
            jennic_chip = request.form.get("jen-chip", False)
            crc = df.loc[(df['Ver'] == jennic_name) & (df['Chiptype'] == jennic_chip), 'CRC']
            length = df.loc[(df['Ver'] == jennic_name) & (df['Chiptype'] == jennic_chip), 'Length']
            crc_string = (crc.to_string(index=False))
            length_string = (length.to_string(index=False))
            jennic_float = float(jennic_name)
            jennic_name_num = math.trunc(jennic_float)
            return render_template("jennic_nde_direct.html",node_mac=mac_addr,j_name=jennic_name_num,j_chip=jennic_chip,crc_name = crc_string,length_name=length_string)

@app.route('/efm-nde-direct',methods=["GET","POST"])
def receive_data_efm_direct_NDE():
    if request.method == "POST":
        if (request.form.get("ef-ver") == "Nothing") or (request.form.get("efm-chip") == "Nothing"):
            flash('Please select valid version')
            return redirect(url_for('home'))
        elif int(len(request.form.get("mac", False))) < 16:
            flash('Minimum 16 digit required for MAC address', category="Error")
            return redirect(url_for('home'))
        else:
            mac_addr = request.form.get("mac", False)
            efm_name = request.form.get("ef-ver",False)
            e_chip_e = request.form.get("efm-chip", False)
            crc = df.loc[(df['Ver'] == efm_name) & (df['Chiptype'] == e_chip_e) , 'CRC']
            length = df.loc[(df['Ver'] == efm_name) & (df['Chiptype'] == e_chip_e) , 'Length']
            crc_string = (crc.to_string(index=False))
            length_string = (length.to_string(index=False))
            efm_float = float(efm_name)
            efm_name_num = math.trunc(efm_float)
            return render_template("efm_nde_direct.html",node_mac=mac_addr,e_name=efm_name_num,e_chip=e_chip_e,cr_name=crc_string,le_name=length_string)


if __name__ == "__main__":
    app.run(debug=True)






