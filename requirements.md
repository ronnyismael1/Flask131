## <remove all of the example text and notes in < > such as this one>

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

1. User home page (user can see messages of users they follow)
- **Pre-condition:** 
  -user is logged in

- **Trigger:**
  -user is on the home page 

- **Primary Sequence:**
  
  1. User is logged in
  2. Redirected to home page
  3. System checks the list of people they follow
  4. System prints out the posts of the people
  5. User can see the posts
  
- **Primary Postconditions:** <can be a list or short description> 
  1. User sees the posts of people who they follow
  
- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. User is not logged in
    a. user does not see the posts
    b. user is redirected to login page

2. Use Case Name (Should match functional requirement name)
   ...
