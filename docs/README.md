# Prizeversity Bits Calculation Integration
This integration will serve as a web application that will streamline the process for CSC level lab instructor TA's to automate bit calculations based on syllabus criteria for input into the Prizeversity platform.

#### Implementation
- The website will be created with the `Django` platform with `Python`.
- The website will be hosted for free on `Github Pages`.
- The files will be processed with `Python` `CSV` and `SQLite` libs.
- Github Actions will be used as CI/CD pipelines using `Python` libs
    - `black`
    - `flake8`
    - `pyright`

#### Bits Calculations
For bits calculations, three criteria need to be checked.
1. First ten students to complete per lab get extra bits
2. Students that maintain perfect submission streaks get extra bits
3. Students that complete both DD for that lab get extra bits

The base amount of bits that students receive simply for completion of a DD varies by semester week.

| Weeks | Bits |
| ------| ---- |
| 1 - 4 | 10 |
| 5 - 8 | 20 |
| 9 - 12 | 30 |

#### Future Features
- Editable criteria values, not hard-coded
- Domain name linked to GitHub pages