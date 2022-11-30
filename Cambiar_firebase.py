import pyrebase

config = {
"apiKey": "AIzaSyBtUBcMDPVuSdsSVTUT_XRoV7RbxSEXRWE",
"authDomain": "esp32-firebase-iot-dc703.firebaseapp.com",
"projectId": "esp32-firebase-iot-dc703",
"databaseURL":"https://esp32-firebase-iot-dc703-default-rtdb.firebaseio.com/",
"storageBucket": "esp32-firebase-iot-dc703.appspot.com",
"messagingSenderId": "40763189353",
"appId": "1:40763189353:web:98991dc8e5bd1c0db85af8",
"measurementId": "G-M8MKTL5LGE"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

all_users = db.child("test").get()
for users in all_users.each():
    print(users.key())
    print(users.val())
    if users.key() == "digito":
        if int(users.val()) > 9:
            db.child("test").update({"Usuario":"El_numero_es_mayor_a_9"})
            print("Data updated successfully ")
