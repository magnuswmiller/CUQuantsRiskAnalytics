# CUQuantsRiskAnalytics
Risk Analytics platform created by and maintained by the CU Quants Risk Analytics Team in coordination with CU Boulder's Leed's Investment and Trading Group (LITG).
This project is actively maintained by a core group of CU Quants members and will be regularly updated moving forward. To join the group on maintainers and contributors, please reach out.
While being developed, outside users can fork the project to develop for their own means. We just ask that if a version of this project is used that the original creators are acknowledged and cited.

---
## Requirements:
- Python (v3.12+)
- Numpy (v)
- Pandas (v)
- datetime (v)
- Yahoo Finance (v)

---
## Project Structure:
This project is comprised of four parts: (1) driver(), (2) Portfolio_Parser(), (3) Portfolio(), and (4) Stock().

- **driver():**
    This file serves as a handler for the calculator. Currently requests user input for prtfolio history csv, current date, and cash on hand which it passes to the parser. These values can be hard-coded instead for other use cases.
    The driver requires the use of the **Portfolio_Parser()**, **Portfolio()**, and **Stock()** classes to work properly.
    If implementing this project into other frameworks, please use the current version of this file to serve as a guide for its use.
- **Portfolio_Parser():**
    This file handles reading the .csv file located at the provided file path and converting it to a more readable and accessible form. This file also handles converting the data into a virtual portfolio (Portfolio object) which is returned to the driver.
    The creation of the Portfolio object requires the import of the Portfolio and Stock classes. For best implementation, please refrain from editing or modifying this file unless you know what you are doing.
- **Portfolio():**
    This file handles the creation of the virtual portfolio objects. This file outlines a class which can be modified by users of this project. The Portfolio class handles the majority of logic regarding the risk calculations.
    As a result, please feel free to edit to cater to your needs. When it comes to implementing portfolio calculations, this is where they are located.
    New/additional calculations can be written as functions within the Portfolio class and can be accessed via driver()->Portfolio_Parser().
- **Stock():**
    This file handles the creation of the virtual stock objects which are instantiated and handled by the Portfolio class. Access to this file should be limited to read-only for best use.
    When writing new calculations within the Portfolio class, feel free to reference this file but refrain from editing it (unless a contributing member to the core group).

The overall data pipeline is summarized below:
**driver()** --> **Portfolio_Parser()** --> **Portfolio()** --> **Stock()**
 (editable)                                   (editable)

---
## Version 0.0
# Release updates
- v0.0 release holds the barebones skeleton of the project. Contains all of the base essentials for development.
- Includes _yahoo finance_ data and no calculations included (will be developed soon)
- No user input or handling for specific calculations
- No 1-page printout of core calculations
- Faulty to string methods of virtual portfolio and virtual stocks
- No handling of saving portfolio for use instead of reloading via trade history (will be implemented soon)

---

