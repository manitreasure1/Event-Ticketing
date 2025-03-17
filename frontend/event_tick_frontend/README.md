# Event Ticketing Frontend

## Routes

The frontend application has the following main routes:
- **Discover**: `/discover`
- **Events**: `/events`
- **Ticket**: `/ticket`
- **Live**: `/live`

## Navbar Behavior

### When User is Logged Out
- The navbar will display a `Login` option.

### When User is Logged In
- The `Login` option will be removed.
- The navbar will display the `User Profile`.

## User Profile

The `User Profile` is a sidenav that includes additional routes:
- **Profile Details**: `/profile`
- **My Tickets**: `/my-tickets`
- **Settings**: `/settings`
- **Logout**: `/logout`

Ensure to implement the necessary authentication checks to toggle the navbar options based on the user's login status.