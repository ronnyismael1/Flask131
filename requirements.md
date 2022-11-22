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
4. Search messages
- **Pre-condition:** <can be a list or short description> 
  -search keyword of atleast one character
  -search keyword can not exceed a total of 500 characters

- **Trigger:** <can be a list or short description>
  -user types in a search keyword in a “search message” bar and presses the search button

- **Primary Sequence:**
  
  1. User is on home page
  2. User types in search keyword 
  3. User clicks search 
  4. System checks if keyword matches any message posts (space sensitive)
  5. System prints out all message posts with search keyword (highlighted)

- **Primary Postconditions:**
  -User sees message posts with all occurances of searched keyword highlighted

- **Alternate Sequence:** 
  
  Search keyword not found in messages
  1. User types in a search keyword 
  2. User clicks search
  3. System checks if keyword matches any message posts
  4. System doesn't find any matches, prompts User with “No messages matched your search”
  
  User searches nothing
  1. User types in nothing in search keyword 
  2. User clicks search
  3. System doesn't search anything
  
  User attempts to search with exceeded character limit
  1. User is typing/pasting in search bar with a keyword that exceeds the 500 character limit
  2. System will only show 500 characters, any extra input will not be accepeted into the search bar
  
  User pastes unformatted text into the search bar
  1. User pastes unformatted text into the search bar
  2. System automatically formats text to default text and font
