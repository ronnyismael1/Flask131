## Functional Requirements

1. Login
2. Logout
3. Create a new account
4. delete account
5. User home page (user can see messages of users they follow)
6. Send messages to followers
7. Follow User
8. Search for user
9. Send/receive private messages
10. Post image with message
11. User profiles
12. Search messages

## Non-functional Requirements

1. Only expected to work on Google Chrome
2. UI interactive interface from Bootstrap
3. Only expected to be formatted properly on desktop
4. Works only with WiFi connection 

## Use Cases

1. Use Case Name (Should match functional requirement name)
- **Pre-condition:** <can be a list or short description> Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua.

- **Trigger:** <can be a list or short description> Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur. 

- **Primary Sequence:**
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Et sequi incidunt 
  3. Quis aute iure reprehenderit
  4. ... 
  5. ...
  6. ...
  7. ...
  8. ...
  9. ...
  10. <Try to stick to a max of 10 steps>

- **Primary Postconditions:** <can be a list or short description> 

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...

- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...

2. Use Case Name: Search user.
- **Pre-condition:**  User is logged in.

- **Trigger:** User clicks on the search icon (a magnifying glass).

- **Primary Sequence:**

  1. System displays a search bar box for the user to enter text.
  2. User types the name of the user they want, in the search bar box and hits enter.
  3. System shows a list of all users with the typed name in the form of their username and actual name.  
  4. User clicks on the desired result.
  5. System opens the result's profile page. 

- **Primary Postconditions:** User sees the profile page of the user they searched for.

- **Alternate Sequence:** 

  1. User entered wrong spelling of the user they want to search.
  2. System shows an error message to the user.

3. Use Case Name: Post image with message.
- **Pre-condition:**  User is logged in and is on the direct message page with another user. 

- **Trigger:** User clicks on the send message bar's photo icon.

- **Primary Sequence:**

  1. System opens the drag and drop field.
  2. User selects an image from Desktop and drags it into the field.
  3. System reserves the image selected to be sent.
  4. User types a message to be sent along with the selected image and clicks on "send".
  5. System sends the text message and the image to another user on the direct message page. 

- **Primary Postconditions:** The image and the message are both sent to the other user. This other user can see these sent to them.

- **Alternate Sequence:** 
  1. User drags and drop a non-photo file into the field.
  2. System shows "Only image files can be dropped" message.
