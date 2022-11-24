## Functional Requirements
1. Login - Adelyn
2. Logout - Adelyn
3. Create a new account
4. delete account
5. User home page (user can see messages of users they follow) - Adelyn
6. Send messages to followers - Ronny
7. Follow User - Ronny
8. Search for user - Sahiti
9. Send/receive private messages
10. Post image with message - Sahiti
11. Open user profile - Ronny
12. Search messages (Homepage) - Brennan

## Non-functional Requirements

1. Only expected to work on Google Chrome
2. UI interactive interface from Bootstrap
3. Only expected to be formatted properly on desktop
4. Works only with WiFi connection 

## Use Cases

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
  
4. Search messages (Homepage)
- **Pre-condition:** 
  -User is logged in

- **Trigger:**
  -User types in a search keyword in a “search message” bar and presses the search button

- **Primary Sequence:**
  
  1. System checks if keyword matches any message posts (space sensitive)
  2. System prints out all message posts with search keyword (highlighted)

- **Primary Postconditions:**
  -User sees message posts with all occurances of searched keyword highlighted

- **Alternate Sequence:** 
  
  Search keyword not found in messages
  1. System checks if keyword matches any message posts
  2. System doesn't find any matches, prompts User with “No messages matched your search”
  
  User searches nothing
  1. System doesn't search anything
  
  User attempts to search with exceeded character limit
  1. User is typing/pasting in search bar with a keyword that exceeds the 500 character limit
  2. System will only show 500 characters, any extra input will not be accepeted into the search bar
  
  User pastes unformatted text into the search bar
  1. User pastes unformatted text into the search bar
  2. System automatically formats text to default text and font

5. Use Case Name: Open User Profile
- **Pre-condition:**  User is logged in and has access to wifi and has an account already created.
 
- **Trigger:**  User clicks on profile icon
 
- **Primary Sequence:**
  1. System identifies their account
  2. System navigates user to their personal user profile
 
- **Primary Postconditions:** User is able to view their personal profile and interact with their page.
 
- **Alternate Sequence:**
  1. User has not created a profile yet when clicking make a post icon
  2. System prompts user to create a profile
 
6. Use Case Name: Send Messages to Followers
- **Pre-condition:**  User is logged into their account and has access to wifi and has an account already created. User is on their home page.
 
- **Trigger:**  User clicks the plus sign button
 
- **Primary Sequence:**
  1. System redirects user to draft screen for your message
  2. User is able to input a series of strings
  3. System saves the inputed information
  4. User clicks on "publish message"
  5. System publishes the message
 
- **Primary Postconditions:** The user's followers are now able to view and interact with the user's message/post
 
- **Alternate Sequence:**
  1. The user inputs too many characters in the post and exceeds the limit
  2. The system prompts the user with an error message
