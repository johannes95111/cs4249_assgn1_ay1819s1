### Project Structure
 The interface is a static web project. However because of cross origin restrictions you will need a web server to run the experiment. Either turn on Github Pages(https://pages.github.com/) for your forked repository or setup a local server of your choice.
 
    ├── css                     # Style Sheets
         ├── external           
         ├── experiment.css    
    ├── js                      # Javascript
         ├── external          
         ├── experiment.js    
         ├── experiment-tracker.js
    ├── data           
         ├── experiments        # Contains multiple sets of experiment trials arrangements
             ├── set1.csv       # Set of experiment trials arrangement for participant 1
             ├── set2.csv       # Set of experiment trials arrangement for participant 2
             ├── set3.csv       # Set of experiment trials arrangement for participant 3
             ├── set4.csv       # Set of experiment trials arrangement for participant 4
             ├── set5.csv       # Set of experiment trials arrangement for participant 5
             ├── set6.csv       # Set of experiment trials arrangement for participant 6
             ├── set7.csv       # Set of experiment trials arrangement for participant 7
             ├── set8.csv       # Set of experiment trials arrangement for participant 8
         ├── menus              # Contains multiple menus for experiment
             ├── menu_depth_1_breadth_4.csv   # Menu with depth 1 breadth 4
             ├── menu_depth_1_breadth_8.csv   # Menu with depth 1 breadth 8
             ├── menu_depth_2_breadth_4.csv   # Menu with depth 2 breadth 4
             ├── menu_depth_2_breadth_8.csv   # Menu with depth 2 breadth 8
             ├── menu_depth_3_breadth_4.csv   # Menu with depth 3 breadth 4
             ├── menu_depth_3_breadth_8.csv   # Menu with depth 3 breadth 8
    ├── documents               # Documentations
         ├── instruction_p1.png # Experiment Instruction Part 1
         ├── instruction_p2.png # Experiment Instruction Part 2
    ├── index.html    

### Changes and Updates
- Added two IVs for the experiment which are 'Menu Breadth' and 'Input Device'
- Added instruction page, pre-experiment survey page and post-experiment survey page
- Added 'Attempt' recording for Marking Menu
- Adjusted text size and font in Marking Menu and Radial menu to keep consistance

### Marking Menu 
- Popup: Left Mouse Down
- Select: Stroke to leaf node
- Reset: Release Mouse Down
- Note:* Expert user's can make a fast stroke instead of waiting for the manu to pop up.

### Radial Menu:
- Popup: Right Click
- Select: Left Click
- Reset: Right Click
   
### Recommended Browsers
This repository has been tested on the browsers listed below. It is suggested you use Chrome.
1. Chrome 68.0.3440.106
2. Firfox 61.0.2
3. Safari V10

### Credits
This repository contains modified implementations of menus from the original contributors listed below.
1. Marking Menu : Forked from https://github.com/QuentinRoy/Marking-Menu
2. Radial Menu : Forked from https://github.com/lgrkvst/d3-sunburst-menu
