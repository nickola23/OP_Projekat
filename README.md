# Gym Booking System

A terminal-based Python application for managing and booking gym group training sessions, designed for use by unregistered users, registered members, instructors, and administrators.

## 📒 Description

This application provides a simple way to manage group training bookings for gyms. Users can browse available programs, register accounts, book training slots, and manage their reservations. Administrators and instructors have additional functionality for managing sessions and memberships.

## ⚡ Features

### General Features (For All Users):
- **Login System:** Users can log in with valid credentials to access their respective roles.
- **Browse Training Programs:** View details like program name, type, duration, and required membership package.
- **Search Programs:** Search training programs by name, type, duration, or membership package.
- **Search Training Sessions:** Filter sessions by program, room, date, or time.

### Unregistered Users:
- **Registration:** Create an account with a username, password, and personal details to become a registered member.

### Registered Members:
- **Book Training Slots:** Reserve spots in group training sessions.
- **View Bookings:** See a list of all reservations, including session details.
- **Cancel Bookings:** Cancel reservations, with checks to prevent cancellation of expired sessions or sessions requiring premium membership.

### Instructors:
- **Manage Reservations:** Book, view, and cancel reservations for their sessions.
- **Activate Memberships:** Extend active membership status for members or upgrade them to premium packages.
- **Edit Reservations:** Modify existing reservations, including session details or assigned users.

### Administrators:
- **Manage Instructors:** Add, update, or remove instructor accounts.
- **Generate Reports:**
  - Daily or weekly reservation summaries.
  - Popular programs or time slots.
  - Member activity and loyalty rewards.
- **Manage Training Programs:** Add, update, or delete training programs and sessions.
- **Award Loyalty:** Automatically award premium memberships to highly active members.

## 🔧 Technologies
- **Language:** Python
- **Environment:** Terminal-based application

## 🔌 How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/nickola23/OP_Projekat.git
   ```
   
2. Run the application:
   ```bash
   python main.py
   ```
   
3. Follow on-screen prompts to navigate through the application.
