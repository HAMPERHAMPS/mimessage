# messaging_platform.py
# Open the file in read mode


ubser = []
import datetime
import pytz
# Now 'users' contains the content of the file
print(ubser)  # You can replace this with any other processing you need
import os
import sys
scre = 0
from flask import Flask, request, render_template_string, jsonify, send_file
import time
banned = []
app = Flask(__name__)

# In-memory storage for messages (replace with a database in production)
messages = []
users = {}  # Store user information (username and messages)
# Define the base variable name
base_name = "skrib"
absa = "banned.txt"
# Define the number of variations
users_credentials_file = "users.txt"
def saveusers(username, password):
    with open(users_credentials_file, 'a') as file:

        file.write(f"{username},{password}\n")
        print("saved " + username + " and password: " + password)
# Print the first few variations

def load_users_credentials():
    if os.path.exists(users_credentials_file):

        with open(users_credentials_file, 'r') as file:

            for line in file:

                username, password = line.strip().split(',')

                # users_credentials[username] = password
                ubser.append({'username': username, 'password': password})
load_users_credentials()



def loadbanned():
    if os.path.exists(absa):

        with open(absa, 'r') as file:

            for line in file:

                nusername = line.strip()

                # users_credentials[username] = password
                banned.append({'banned': nusername})

loadbanned()

def savebanned(username):
    with open(absa, 'a') as file:

        file.write(f"{username}\n")
        print("saved " + username)
# Print the first few variations
# HTML template for the messaging platform


def roletest(sender):
    if sender == "HAMPER":
        return "Owner"
    elif sender == "Victoria obsessed Watcher" or sender == "Pineapple":
        return "Admin"
    elif sender == "jayden" or sender == "1696300":
        return "Mod"
    else:
        return "Standard"



html_template = """
<!DOCTYPE html>
<html>
<head>
<link rel="icon" type="image/png" href="https://hamperhamps.github.io/contents/c.png">

    <title>MiMessage</title>
    <meta name="description" content="Free room based messaging. Supports FelixEnder Reviews">
  <meta name="keywords" content="HTML, CSS, JavaScript, message, messaging, rooms, chatrooms, python">
  <meta name="author" content="HAMPER">

</head>
<style>
    * {
    color: white;
}

</style>


    <style>
        /* Reset default input styles */
        input {
            border: none;
            outline: none;
            padding: 10px;
            font-size: 16px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        /* Style the input text bar */
        .input-bar {
            display: inline-block;
            background-color: #f5f5f5;
        }

        /* Add placeholder text style */
        .input-bar input::placeholder {
            color: #999;
        }
body {
    overflow-x: hidden; /* Hide horizontal scrollbar */
}


    </style>

    <style>
        /* Style for the button */
        .nice-blue-button {
            display: inline-block;
            padding: 10px 20px;
            font-family: Tahoma, sans-serif;
            font-size: 16px;
            background-color: #0074D9; /* Blue color */
            color: #ffffff; /* White text */
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        /* Hover effect */
        .nice-blue-button:hover {
            background-color: #0056b3; /* Darker blue on hover */
        }
    </style>
</html>

<body style="background-color: black">

    <h1 style="font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">MiMessage</h1>

    <center><iframe  id="thatoneguy" src="/sigma"></iframe></center>
    <div id="chat">


        <input class="input-bar" type="text" style="color: grey; background-color: #373737;" id="message"  placeholder="Type your message...">
        <button style="color: black" onclick="sendMessage()" id="sendbutton" class="nice-blue-button">Send</button>

    </div>
    <canvas height="5px"></canvas>
    <center><div id="chat">
        <button style="color: black; background-color: red;" onclick="signout()" class="nice-blue-button">Sign Out</button>

    </div></center>
    <img src="https://hamperhamps.github.io/contents/c.png" style="position: absolute; top: 20px; right: 20px;" height="51px" width="70px"></img>
    <p style="position: absolute; bottom: 0; right: 0; font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;">Made by HAMPER</p>
<center><p style="font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;">Btw if you want to use private rooms type any number after the url to be taken to that private room.</p><p style="color: red; font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;">MESSAGES ARE NOT FOREVER WHEN THE SERVER RESTARTS ALL MESSAGES ARE DELETED</p><a href="https://discord.gg/4Er5DaBPyh"><p style="color: yellow; font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;">Join me Discord server.</p></a></center>

<script>
  const input = document.getElementById("message");
  input.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {

      document.getElementById("sendbutton").click(); // Trigger button click
    }
  });
</script>
<script>
function signout() {
    localStorage.setItem('signedin', 0);
    localStorage.setItem('username', "Some Guy");
    localStorage.setItem('password', 0);
    window.location.href = "https://hamperhamps.pythonanywhere.com/login";
}
</script>
    <script>
var width = window.innerWidth - 25; // Adjust the margin as needed
var siggs = document.getElementById("thatoneguy");
siggs.style.width = width + "px";

var height = window.innerHeight - 140; // Adjust the margin as needed
siggs.style.height = height + "px";
var widths = window.innerWidth - 250; // Adjust the margin as needed
var sigger = document.getElementById("message");
sigger.style.width = widths + "px";
    </script>
            <script>
    let signed = localStorage.getItem('signedin')
    if (typeof signed !== 'undefined') {
        console.log("heeeeb");

    }
    else {
        window.location.href = "https://hamperhamps.pythonanywhere.com/login";
    }
    </script>

    <script>
        // Get the username from local storage or set a default value
        let userId = localStorage.getItem('username') || 'Some Guy';
        if (userId == "Some Guy") {
            window.location.href = "https://hamperhamps.pythonanywhere.com/login";
        }
        if (userId == "{{ bann }}") {
            window.location.href = "https://hamperhamps.pythonanywhere.com/login";
        }
        function sendMessage() {
            const messageInput = document.getElementById('message');
            const messageText = messageInput.value.trim();
            if (messageText) {
                fetch('/send_message', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ sender: userId, text: messageText })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.message) {
                        messageInput.value = '';
                    }
                });
            }

        }


    </script>
    <script>
    if (localStorage.getItem('baned') == 1) {
        localStorage.setItem('signedin', 0);
        window.location.href = "https://hamperhamps.pythonanywhere.com/login";
    }
    </script>
    <script>
    function oauthcheck() {
        console.log("Checking oauth");
        meme = localStorage.getItem('username');
        momo = localStorage.getItem('password');
        if (meme && momo) {
        fetch('/login/post/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: meme, password: momo })
        })
        .then(response => response.json())
        .then(data => {
            if (data === 'Success') {
                console.log("ok yur in");

            } else {

                console.log("Login failed:", data);
            }
            if (data === 'thatsme') {
                localStorage.setItem('signedin', 0);
                localStorage.setItem('username', "Some Guy");
                localStorage.setItem('password', 0);
                window.location.href = "https://hamperhamps.pythonanywhere.com/login";


            }
            if (data === 'banned') {
                localStorage.setItem('signedin', 0);
                localStorage.setItem('username', "Some Guy");
                localStorage.setItem('password', 0);
                window.location.href = "https://hamperhamps.pythonanywhere.com/login";
                localStorage.setItem('baned', 1);
            }
        })
        .catch(error => {

            localStorage.setItem('signedin', 0);
            localStorage.setItem('username', "Some Guy");
            localStorage.setItem('password', 0);
            window.location.href = "https://hamperhamps.pythonanywhere.com/login";
            console.error('Error:', error);
        });
    } else {
        localStorage.setItem('signedin', 0);
        localStorage.setItem('username', "Some Guy");
        localStorage.setItem('password', 0);
        window.location.href = "https://hamperhamps.pythonanywhere.com/login";
        console.log("Username or password is empty");
    }
}

oauthcheck()
    </script>
</body>
</html>
"""
htmlsigma = """
<style>
    body {
    overflow: hidden; /* Hide scrollbars */
}
</style>
    <div id="content">
        <div id="messages">
            {% for msg in messagess %}

                <p style="color: white; font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;">[{{ msg.role }}] ({{ msg.time }}) {{ msg.sender }}: {{ msg.text }}</p>
            {% endfor %}
        </div>
    </div>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<script>
// Refresh the content every second without a button

function refreshContent() {
    // Save the current scroll position
    const scrollPosition = $(window).scrollTop();

    // Load the new content (e.g., new messages) without a full page reload
    $('#content').load(window.location.href + ' #content', function() {
        // Restore the scroll position
        $(window).scrollTop(scrollPosition);
    });
}

// Refresh every second
setInterval(refreshContent, 1000);
</script>
<script>
    function scrollPage() {
    $("html, body").animate({ scrollTop: $(document).height() }, 1000);
}

// Repeat the function every second (1000 milliseconds)
setInterval(scrollPage, 1000);

</script>


"""

@app.route('/')
def index():
    return render_template_string(html_template, messages=messages, bann=banned)
@app.route('/sigma')
def sigma():

    return render_template_string(htmlsigma, messagess=messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        sender = data.get('sender')
        text = data.get('text')
        print(sender + " sent " + text)
        if not sender or not text:
            return jsonify({'error': 'Invalid message data'}), 400
        new_message = sender + ": " + text
        # Store the message
        est = pytz.timezone('America/New_York')
        current_time_est = datetime.datetime.now(est)

        # Format the time as "12:34 PM"
        current_time_est = datetime.datetime.now(est)

        # Format the time as "12:34 PM"
        formatted_time = current_time_est.strftime("%I:%M %p")

        adma = roletest(sender)
        messages.append({'sender': sender, 'text': text, 'role': adma, 'time': formatted_time})

        return jsonify({'message': 'Message sent successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

apps = "1"
approute = '/send_message/' + apps

current_room_id = []
htmlpriv = """<!DOCTYPE html>
<html>
<head>

<link rel="icon" type="image/png" href="https://hamperhamps.github.io/contents/c.png">

    <title>MiMessage (Private channel)</title>
    <meta name="description" content="Free room based messaging. Supports FelixEnder Reviews">
  <meta name="keywords" content="HTML, CSS, JavaScript, message, messaging, rooms, chatrooms, python">
  <meta name="author" content="HAMPER">

</head>
<style>
    * {
    color: white;
}

</style>


    <style>
        /* Reset default input styles */
        input {
            border: none;
            outline: none;
            padding: 10px;
            font-size: 16px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        /* Style the input text bar */
        .input-bar {
            display: inline-block;
            background-color: #f5f5f5;
        }

        /* Add placeholder text style */
        .input-bar input::placeholder {
            color: #999;
        }
body {
    overflow-x: hidden; /* Hide horizontal scrollbar */
}


    </style>

    <style>
        /* Style for the button */
        .nice-blue-button {
            display: inline-block;
            padding: 10px 20px;
            font-family: Tahoma, sans-serif;
            font-size: 16px;
            background-color: #0074D9; /* Blue color */
            color: #ffffff; /* White text */
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        /* Hover effect */
        .nice-blue-button:hover {
            background-color: #0056b3; /* Darker blue on hover */
        }
    </style>
<body style="background-color: black">

    <h1 style="font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">MiMessage (Private channel)</h1>
    <iframe id="ifrat"></iframe>
    <div id="chat">


        <input class="input-bar" type="text" style="color: grey; background-color: #373737;" id="message"  placeholder="Type your message...">
        <button style="color: black" onclick="sendMessage()" id="sendbutton" class="nice-blue-button">Send</button>

    </div>
        <script>
    if (localStorage.getItem('baned') == 1) {
        localStorage.setItem('signedin', 0);
        window.location.href = "https://hamperhamps.pythonanywhere.com/login";

    }
    </script>
    <script>
    function oauthcheck() {
        console.log("Checking oauth");
        meme = localStorage.getItem('username');
        momo = localStorage.getItem('password');
        if (meme && momo) {
        fetch('/login/post/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: meme, password: momo })
        })
        .then(response => response.json())
        .then(data => {
            if (data === 'Success') {
                console.log("ok yur in");

            } else {

                console.log("Login failed:", data);
            }
            if (data === 'thatsme') {
                localStorage.setItem('signedin', 0);
                localStorage.setItem('username', "(I dont know how to change my username)");
                localStorage.setItem('password', 0);
                window.location.href = "https://hamperhamps.pythonanywhere.com/login";


            }
            if (data === 'banned') {
                localStorage.setItem('signedin', 0);
                localStorage.setItem('username', "(I dont know how to change my username)");
                localStorage.setItem('password', 0);
                localStorage.setItem('baned', 1);

                window.location.href = "https://hamperhamps.pythonanywhere.com/login";
            }
        })
        .catch(error => {

            localStorage.setItem('signedin', 0);
            localStorage.setItem('username', "(I dont know how to change my username)");
            localStorage.setItem('password', 0);
            window.location.href = "https://hamperhamps.pythonanywhere.com/login";
            console.error('Error:', error);
        });
    } else {
        localStorage.setItem('signedin', 0);
        localStorage.setItem('username', "(I dont know how to change my username)");
        localStorage.setItem('password', 0);
        window.location.href = "https://hamperhamps.pythonanywhere.com/login";
        console.log("Username or password is empty");
    }
}

oauthcheck()
    </script>
    <script>
  const input = document.getElementById("message");
  input.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {

      document.getElementById("sendbutton").click(); // Trigger button click
    }
  });
</script>
    <canvas height="5px"></canvas>
    <center><div id="chat">
        <button style="color: black; background-color: red;" onclick="signout()" class="nice-blue-button">Sign Out</button>
    </div></center>
    <p style="position: absolute; bottom: 0; right: 0; font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;">Made by HAMPER</p>
    <center><p style="font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;">Btw if you want to use private rooms type any number after the url to be taken to that private room.</p><p style="color: red; font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;">MESSAGES ARE NOT FOREVER WHEN THE SERVER RESTARTS ALL MESSAGES ARE DELETED</p></center>
    <p style="font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;">Current room id: <a id="showid"></a> </p>
    <img src="https://hamperhamps.github.io/contents/c.png" style="position: absolute; top: 20px; right: 20px;" height="51px" width="70px"></img>
        <script>
    let signed = localStorage.getItem('signedin')
        if (typeof signed !== 'undefined') {
            console.log("heeeeb");

        }
        else {
            window.location.href = "https://hamperhamps.pythonanywhere.com/login";
        }
    </script>
    <script>
        var currentURL = document.URL;
        var part = currentURL.split("/")[3];
        document.getElementById("showid").textContent = part;
        var gege = "/sigma/" + part;
        document.getElementById("ifrat").src = gege;
        // Get the username from local storage or set a default value
        let userId = localStorage.getItem('username') || '(I dont know how to change my username)';
        if (userId == "(I dont know how to change my username)") {
            window.location.href = "https://hamperhamps.pythonanywhere.com/login";
        }
        if (userId == bann) {
            window.location.href = "https://hamperhamps.pythonanywhere.com/login";
        }
        function sendMessage() {
            const messageInput = document.getElementById('message');
            const messageText = messageInput.value.trim();
            if (messageText) {
                fetch('/send_message/' + part, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ sender: userId, text: messageText, room: part })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.message) {
                        messageInput.value = '';
                    }
                });
            }

        }


    </script>


    <script>
        function signout() {
            localStorage.setItem('signedin', 0);
            localStorage.setItem('username', '(I dont know how to change my username)');
            localStorage.setItem('password', 0);
            window.location.href = "https://hamperhamps.pythonanywhere.com/login";
        }
    </script>
    <script>
var width = window.innerWidth - 25; // Adjust the margin as needed
var siggs = document.getElementById("ifrat");
siggs.style.width = width + "px";

var height = window.innerHeight - 140; // Adjust the margin as needed
siggs.style.height = height + "px";
var widths = window.innerWidth - 250; // Adjust the margin as needed
var sigger = document.getElementById("message");
sigger.style.width = widths + "px";
    </script>
</body>
</html>"""
htmlsigmapriv = """
<style>
    body {
    overflow: hidden; /* Hide scrollbars */
}
</style>
    <div id="content">
        <div id="messages">
            {% for msg in sds %}
                <p style="color: white; font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;">[{{ msg.role }}] ({{ msg.time }}) {{ msg.sender }}: {{ msg.text }}</p>
            {% endfor %}
        </div>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    </div>
<script>
    function scrollPage() {
    $("html, body").animate({ scrollTop: $(document).height() }, 1000);
}

// Repeat the function every second (1000 milliseconds)
setInterval(scrollPage, 1000);

</script>

        <script>



// Extract room IDs

// Display room IDs

            skid = 0;
            console.log({{sos}});
            console.log({{sds}});
        </script>
        <script>
        // Refresh the content every second without a button
function refreshContent() {
    // Save the current scroll position
    const scrollPosition = $(window).scrollTop();

    // Load the new content (e.g., new messages) without a full page reload
    $('#content').load(window.location.href + ' #content', function() {
        // Restore the scroll position
        $(window).scrollTop(scrollPosition);
    });
}

// Refresh every second
setInterval(refreshContent, 1000);
</script>

"""
testroute = False
if testroute == True:
    apps = input("test route:")
stop = 0
abbr = 1
def filter_messages_by_room(messages, target_room):
    filtered_messages = [msg for msg in messages if msg['room'] == target_room]
    return filtered_messages
def filter_messages(messages, target_room):
    filtered_message = [msg for msg in messages if msg['sender'] == target_room]
    return filtered_message
def filter_messagestext(messages, target_room):
    filtered_messa = [msg for msg in messages if msg['text'] == target_room]
    return filtered_messa
@app.route('/<int:room_id>')
def chat_room(room_id):
    global current_room_id
    current_room_id = str(room_id)
    print("Current room id: " + str(current_room_id))
    return render_template_string(htmlpriv, room_id=room_id, message=message, banned=banned)
message = []
@app.route('/sigma/<int:room_id>')
def chat_roomed(room_id):
    print("MESSAGE_____________________________________ " + str(message))
    print("RROROROROR " + str(room_id))
    print("Coontacted private room")
    nono = 0
    for msg in message:
        print(msg)
        name_value = msg['room']
        print(name_value)
        nono = name_value
        print("STARTING SEC 2-------------------------------------------")
    matching_messages = filter_messages_by_room(message, str(room_id))

    print("HERE---------------" + str(matching_messages) + str(room_id))



    return render_template_string(htmlsigmapriv, roomie=room_id, messager=message, sds=matching_messages, sos=nono)


messa = []
@app.route('/send_message/<int:room_ids>', methods=['POST'])
def sender(room_ids):
    try:
        data = request.get_json()
        sender = data.get('sender')
        text = data.get('text')
        room = data.get('room')
        print(f"{sender} sent '{text}' in room {room_ids}")

        if not sender or not text:
            return jsonify({'error': 'Invalid message data'}), 400
        adma = roletest(sender)
        # Store the message
        est = pytz.timezone('America/New_York')
        current_time_est = datetime.datetime.now(est)

        # Format the time as "12:34 PM"
        current_time_est = datetime.datetime.now(est)

        # Format the time as "12:34 PM"
        formatted_time = current_time_est.strftime("%I:%M %p")
        message.append({'sender': sender, 'text': text, 'room': room, 'role': adma, 'time': formatted_time})

        return jsonify({'message': 'Message sent successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

four = """<!DOCTYPE html>
<head>
<title>Not Found :\</title>
</head>
<body style="background-color: black;">
<center><h1 style="color: red; font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">Error 404: Not found</h1>
<img src="https://hamperhamps.github.io/contents/d.png" width="300px" height="300px"></img></center>
</body>"""

login = """<!DOCTYPE html>
<head>
<link rel="icon" type="image/png" href="https://hamperhamps.github.io/contents/c.png">
<title>Login to MiMessage</title>
</head>
<body style="background-color: black;">

    <style>
        /* Reset default input styles */
        input {
            border: none;
            outline: none;
            padding: 10px;
            font-size: 16px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        /* Style the input text bar */
        .input-bar {
            display: inline-block;
            background-color: #f5f5f5;
        }

        /* Add placeholder text style */
        .input-bar input::placeholder {
            color: #999;
        }
body {
    overflow-x: hidden; /* Hide horizontal scrollbar */
}


    </style>
    <style>
        /* Reset default input styles */
        input {
            border: none;
            outline: none;
            padding: 10px;
            font-size: 16px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            display: block;
            margin: 0 auto;
        }

        /* Style the input text bar */
        .input-bar {
            display: inline-block;
            background-color: #f5f5f5;
        }

        /* Add placeholder text style */
        .input-bar input::placeholder {
            color: #999;
        }
body {
    overflow-x: hidden; /* Hide horizontal scrollbar */
}


    </style>

    <style>
        /* Style for the button */
        .nice-blue-button {
            display: inline-block;
            padding: 10px 20px;
            font-family: Tahoma, sans-serif;
            font-size: 16px;
            background-color: #0074D9; /* Blue color */
            color: #ffffff; /* White text */
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        /* Hover effect */
        .nice-blue-button:hover {
            background-color: #0056b3; /* Darker blue on hover */
        }
        div.wrapper {
            width: 300px;
            height: 300px;
            border: 1px solid black;
        }
    </style>
    <canvas height="30px"></canvas>
<center><img src="https://hamperhamps.github.io/contents/c.png"></img></center>
<canvas height="30px"></canvas>
    <center><div class="wrapper" style="background-color: #656665;">
        <center><h2 style="font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;">MiMessage (Sign Up)</h2></center>
        <input class="input-bar" style="background-color: #9FA09F;" type="text" id="username"  placeholder="Username">
        <canvas height="1px"></canvas>
        <input class="input-bar" style="background-color: #9FA09F;" type="password" id="password"  placeholder="Password">
        <p style="font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;" id="bbc">By continuing you agree to the TOS</p>
        <a style="font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif; color: red;" href="/tos">TOS</a>
        <center><button style="color: black" onclick="login()" class="nice-blue-button">Sign Up</button></center>
        <center><a href="https://hamperhamps.pythonanywhere.com/login/login">Login</a></center>
    </div></center>
    <script>
    let signed = localStorage.getItem('signedin')
    if (signed == 1) {
        window.location.href = "https://hamperhamps.pythonanywhere.com";
    }
    </script>
    <script>
function login() {
    console.log("logging in");
    const messageInput = document.getElementById('username');
    const messageText = messageInput.value.trim();
    const passwordInput = document.getElementById('password');
    const passwordText = passwordInput.value.trim();

    if (messageText && passwordText) {
        fetch('/login/post', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: messageText, password: passwordText })
        })
        .then(response => response.json())
        .then(data => {
            if (data === 'Success') {
                console.log("ok yur in");
                localStorage.setItem('signedin', 1);
                localStorage.setItem('username', messageText);
                localStorage.setItem('password', passwordText);
                window.location.href = "https://hamperhamps.pythonanywhere.com";
            } else {
                console.log("Login failed:", data);
            }
            if (data === 'thatsme') {
                console.log('nono');
                document.getElementById("bbc").textContent = "Sorry bub you cannot do that it already here you unoriginal peasant";
                document.getElementById("bbc").style.color = "red";


            }
            if (data === 'banned') {
                document.getElementById("bbc").textContent = "L bro imagine getting banned";
                document.getElementById("bbc").style.color = "red";
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    } else {
        console.log("Username or password is empty");
    }
}



</script>
"""
loginlogin = """
<!DOCTYPE html>
<head>
<link rel="icon" type="image/png" href="https://hamperhamps.github.io/contents/c.png">
<title>Login to MiMessage</title>
</head>
<body style="background-color: black;">

    <style>
        /* Reset default input styles */
        input {
            border: none;
            outline: none;
            padding: 10px;
            font-size: 16px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        /* Style the input text bar */
        .input-bar {
            display: inline-block;
            background-color: #f5f5f5;
        }

        /* Add placeholder text style */
        .input-bar input::placeholder {
            color: #999;
        }
body {
    overflow-x: hidden; /* Hide horizontal scrollbar */
}


    </style>
    <style>
        /* Reset default input styles */
        input {
            border: none;
            outline: none;
            padding: 10px;
            font-size: 16px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            display: block;
            margin: 0 auto;
        }

        /* Style the input text bar */
        .input-bar {
            display: inline-block;
            background-color: #f5f5f5;
        }

        /* Add placeholder text style */
        .input-bar input::placeholder {
            color: #999;
        }
body {
    overflow-x: hidden; /* Hide horizontal scrollbar */
}


    </style>

    <style>
        /* Style for the button */
        .nice-blue-button {
            display: inline-block;
            padding: 10px 20px;
            font-family: Tahoma, sans-serif;
            font-size: 16px;
            background-color: #0074D9; /* Blue color */
            color: #ffffff; /* White text */
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        /* Hover effect */
        .nice-blue-button:hover {
            background-color: #0056b3; /* Darker blue on hover */
        }
        div.wrapper {
            width: 300px;
            height: 300px;
            border: 1px solid black;
        }
    </style>
    <canvas height="30px"></canvas>
<center><img src="https://hamperhamps.github.io/contents/c.png"></img></center>
<canvas height="30px"></canvas>
    <center><div class="wrapper" style="background-color: #656665;">
        <center><h2 style="font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;">MiMessage (Log In)</h2></center>
        <input class="input-bar" style="background-color: #9FA09F;" type="text" id="username"  placeholder="Username">
        <canvas height="1px"></canvas>
        <input class="input-bar" style="background-color: #9FA09F;" type="password" id="password"  placeholder="Password">
        <p style="font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;" id="bbc">By continuing you agree to the TOS</p>
        <a style="font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif; color: red;" href="/tos">TOS</a>
        <center><button style="color: black" onclick="login()" class="nice-blue-button">Login</button></center>

    </div></center>
    <script>
    let signed = localStorage.getItem('signedin')
    if (signed == 1) {
        window.location.href = "https://hamperhamps.pythonanywhere.com";
    }
    </script>
    <script>
function login() {
    console.log("logging in");
    const messageInput = document.getElementById('username');
    const messageText = messageInput.value.trim();
    const passwordInput = document.getElementById('password');
    const passwordText = passwordInput.value.trim();

    if (messageText && passwordText) {
        fetch('/login/post/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: messageText, password: passwordText })
        })
        .then(response => response.json())
        .then(data => {
            if (data === 'Success') {
                console.log("ok yur in");
                localStorage.setItem('signedin', 1);
                localStorage.setItem('username', messageText);
                localStorage.setItem('password', passwordText);
                window.location.href = "https://hamperhamps.pythonanywhere.com";
            } else {
                console.log("Login failed:", data);
            }
            if (data === 'thatsme') {
                console.log('nono');
                document.getElementById("bbc").textContent = "That account dont exist";
                document.getElementById("bbc").style.color = "red";


            }
            if (data === 'banned') {
                document.getElementById("bbc").textContent = "L bro imagine getting banned";
                document.getElementById("bbc").style.color = "red";
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    } else {
        console.log("Username or password is empty");
    }
}



</script>
"""

yessir = 0
@app.route('/login/post', methods=['POST'])
def postlogin():
    try:
        # Parse the JSON data from the request
        data = request.get_json()
        password = data.get('password')
        username = data.get('username')

        # Check if the username already exists in 'ubser'
        if any(user['username'] == username for user in ubser):
            # Username found, return a failure response
            return jsonify('thatsme')
        else:


            # Username not found, append new user and return success
            #ubser.append({'username': username, 'password': password})

            ubser.append({'username': username, 'password': password})
            time.sleep(2)
            saveusers(username, password)
            time.sleep(2)
            return jsonify('Success')

        print(ubser)
    except Exception as e:
        # Return the error message and a 500 Internal Server Error status
        return jsonify({'error': str(e)}), 500

@app.route('/login')
def logins():
    return render_template_string(login)
@app.route('/login/login')
def logasins():
    return render_template_string(loginlogin)

banban = """<!DOCTYPE html>
<head>
<title>Ban Ppl</title>
</head>
<body>
<center><input id="baninput"></input><button id="banbutton">Ban User</button>"""






@app.route('/login/post/login', methods=['POST'])
def possstlogin():
    try:
        # Parse the JSON data from the request
        data = request.get_json()
        password = data.get('password')
        username = data.get('username')

        # Check if the username already exists in 'ubser'
        if any(user['username'] == username for user in ubser):
            # Username found, return a failure response
            for usr in ubser:

                if usr['username'] == username:
                    if usr['password'] == password:
                        for ban in banned:
                            if ban['banned'] == username:
                                return jsonify('banned')
                        print("YESSSSS")
                        return jsonify('Success')




        print(ubser)
    except Exception as e:
        # Return the error message and a 500 Internal Server Error status
        return jsonify('thatsme')


@app.errorhandler(404)
def not_found(e):
    return render_template_string(four), 404


nomen = """<!DOCTYPE html>
<head>
<title>This mf really tried</title>
</head>
<body style="background-color: black">
<h1 style="color: red;">Sorry bud but no hamper buh im hamper not u</h1>
</body>"""
heh = """<!DOCTYPE html>
<p style="display: none;" id="sigs"> {{ ubs }} </p>
<script>
const geb = localStorage.getItem('username');
if (geb === "HAMPER") {
    console.log("k");
    const sigsElement = document.getElementById("sigs");
    sigsElement.style.display = "block";
} else {
    const sigsElement = document.getElementById("sigs");
    sigsElement.style.display = "none";
    window.location.href = "https://hamperhamps.pythonanywhere.com";
}

</script>
"""
@app.route("/imhamp")
def hamphamp():
    return render_template_string(nomen)
@app.route('/debug')
def defug():

    return render_template_string(heh, ubs=ubser)


tetty = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tetris Game</title>
    <style>
        /* Styling for the game board */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
        }
        .cell {
            width: 30px;
            height: 30px;
            border: 1px solid #ccc;
            box-sizing: border-box;
        }
    </style>
</head>
<body>
    <script>
        // Tetromino shapes (represented as arrays of cells)
        const tetrominos = [
            [[1, 1, 1, 1]], // I-shape
            [[1, 1, 1], [0, 1, 0]], // T-shape
            // Add more shapes (L, J, S, Z, O)
        ];

        // Initialize game board (2D array)
        const rows = 20;
        const cols = 10;
        const board = Array.from({ length: rows }, () => Array(cols).fill(0));

        // Current tetromino position
        let currentTetromino = tetrominos[0];
        let currentRow = 0;
        let currentCol = Math.floor(cols / 2) - 1;

        // Draw the game board
        function drawBoard() {
            const boardContainer = document.body;
            boardContainer.innerHTML = ''; // Clear previous board

            for (let row = 0; row < rows; row++) {
                for (let col = 0; col < cols; col++) {
                    const cell = document.createElement('div');
                    cell.className = 'cell';
                    cell.style.backgroundColor = board[row][col] ? 'blue' : 'white';
                    boardContainer.appendChild(cell);
                }
            }
        }

        // Update the game loop
        function update() {
            // Move tetromino down
            currentRow++;
            // Check for collisions and handle line clears
            // ...
            drawBoard(); // Update display
        }

        // Keyboard event listener
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowLeft') {
                // Move tetromino left
                // ...
            } else if (e.key === 'ArrowRight') {
                // Move tetromino right
                // ...
            } else if (e.key === 'ArrowDown') {
                // Move tetromino down faster
                // ...
            } else if (e.key === 'ArrowUp') {
                // Rotate tetromino
                // ...
            }
        });

        // Start the game loop
        setInterval(update, 500);
    </script>
</body>
</html>


"""

@app.route('/mitris')
def tete():
    return render_template_string(tetty)


@app.route('/authtest', methods=['POST'])
def authtests():
    data = request.get_json()
    username = data.get('username')

    role = roletest(username)
    if role in ["Owner", "Admin"]:

        return jsonify('yes')
    else:

        return jsonify('no')

@app.route('/authtest/ban', methods=['POST'])
def authtestsvv():
    data = request.get_json()
    username = data.get('username')

    role = roletest(username)
    if role in ["Owner", "Admin", "Mod"]:

        return jsonify('yes')
    else:

        return jsonify('no')

bebe = """<!DOCTYPE html>
<head>
<title>DMS</title>
</head>
<p style="display: none;" id="neb">Private messsages:</p>
<p style="display: none;" id="beb">{{ reds }}</p>
<script>
    function esa() {
        console.log("sadasd");
        const meme = localStorage.getItem('username');
        fetch('/authtest', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: meme })
        })
        .then(response => response.json())
        .then(data => {
            if (data === 'yes') {
                console.log("ASDASDAD");
                const sigsElement = document.getElementById("neb");
                sigsElement.style.display = "block";
                const sigsElemen = document.getElementById("beb");
                sigsElemen.style.display = "block";
            } else {
                console.log("Login failed:", data);
                window.location.href = "https://hamperhamps.pythonanywhere.com";
            }
            if (data === 'no') {
                console.log('nono');
                window.location.href = "https://hamperhamps.pythonanywhere.com";



            }

        })
        .catch(error => {
            console.error('Error:', error);
        });
}
esa()
</script>
"""
@app.route('/read')
def asdsdds():
    return render_template_string(bebe, reds=message)

banner = """
<head>
<title>Ban User</title>


</head>
<body style="background-color: black;">
<center><input class="input-bar" type="text" style="color: grey; background-color: #373737; display: none;" id="banna"  placeholder="Ban">
        <button style="color: black; display: none;" onclick="ban()" id="sendbutton" class="nice-blue-button">Ban</button></center>
        <p style="color: white;">{{ sugs }}</p>
</body>
<script>
function ban() {
                const messageInput = document.getElementById('banna');
            const messageText = messageInput.value.trim();
            if (messageText) {
                fetch('/ban/ban', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ user: messageText })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.message) {
                        messageInput.value = '';
                    }
            if (data === 'sus') {
                console.log("ASDASDADgggggggg");
                const sigsElement = document.getElementById("banna");
                sigsElement.style.color = "green";
                const sigsElemen = document.getElementById("sendbutton");
                sigsElemen.style.color = "green";
            } else {
                console.log("Login failed:", data);

                }
            })
}
}
</script>
<script>
    function esa() {
        console.log("sadasd");
        const meme = localStorage.getItem('username');
        fetch('/authtest/ban', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: meme })
        })
        .then(response => response.json())
        .then(data => {
            if (data === 'yes') {
                console.log("ASDASDAD");
                const sigsElement = document.getElementById("banna");
                sigsElement.style.display = "block";
                const sigsElemen = document.getElementById("sendbutton");
                sigsElemen.style.display = "block";
            } else {
                console.log("Login failed:", data);
                window.location.href = "https://hamperhamps.pythonanywhere.com";
            }
            if (data === 'no') {
                console.log('nono');
                window.location.href = "https://hamperhamps.pythonanywhere.com";



            }

        })
        .catch(error => {
            console.error('Error:', error);
        });
}
esa()
</script>"""
@app.route('/ban/ban', methods=['POST'])
def Sosomay():
    data = request.get_json()
    username = data.get('user')
    if username == "HAMPER":
        return jsonify('no')
    else:
        banned.append({'banned': username})
        savebanned(username)
        return jsonify('sus')



@app.route('/ban')
def ashdahd():
    return render_template_string(banner, sugs=banned)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100, debug=False)

