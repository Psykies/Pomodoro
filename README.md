# Pomodoro

Sure, here's the GitHub README file for the Pomodoro Timer code:

```markdown
# Pomodoro Timer

This is a simple Pomodoro Timer application built using Python's Tkinter library. It helps users manage their work and break intervals following the Pomodoro Technique.

## Functionality

### Timer Mechanism
- Utilizes the Pomodoro Technique, consisting of work intervals, short breaks, and long breaks.
- Each work interval lasts for 25 minutes (`WORK_MIN`), followed by a 5-minute short break (`SHORT_BREAK_MIN`).
- After completing four work intervals, a 20-minute long break (`LONG_BREAK_MIN`) is provided.
- The session finishes after 9 intervals.

### Countdown Mechanism
- Displays the countdown timer in the format `mm:ss`.
- Updates the timer every second until the countdown reaches zero.

### Reset
- Stops the timer and resets the session count, allowing users to start a new Pomodoro session.

### Marks
- Keeps track of completed work intervals with ✓ marks displayed below the timer.

## UI Design
- The UI features a tomato image representing the Pomodoro timer.
- Labels and buttons are styled with colors representing different timer states (work, short break, long break).
- Users can start, pause, reset the timer, and visualize completed intervals.

## Dependencies
- Python 3.x
- Tkinter library

## How to Use
1. Run the Python script `pomodoro_timer.py`.
2. Click on the "Start" button to begin the Pomodoro session.
3. The timer will switch between work intervals, short breaks, and long breaks automatically.
4. Click on the "Reset" button to start a new Pomodoro session.

## Example
https://github.com/Psykies/Pomodoro/assets/32191652/6c400837-52a1-40a5-8861-d75f93b7efe1
https://github.com/Psykies/Pomodoro/assets/32191652/b01262c8-cf39-4516-bc42-1b01980cd31f

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
