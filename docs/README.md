# Prizeversity Bits Calculation Integration
This integration will serve as a web application that will streamline the process for CSC lab instructor TAs to automate bit calculations based on adjustable criteria for easier grade calculation for students. This integration is for the Prizeversity LMS with a future stretch goal of complete integration into the PLMS (not a separate website + automatically update Canvas LMS grades).

#### Implementation
- Coded with the `Django` platform with `Python`.
- Hosted on `PythonAnywhere`, likely on the `Developer` plan.
- Custom domain name, unknown from where, will be linked to `PythonAnywhere` instance.
- The files will be processed with `Python`, `CSV` and `SQLite` libs.

#### Bits Calculations
For bits calculations, three criteria need to be checked.
1. First ten students to complete per lab get extra bits
2. Students that maintain perfect submission streaks get extra bits
3. Students that complete both DD for that lab get extra bits
For more information, please check the `updated_reward_criteria.pdf` under the `docs` folder.

#### Project Management
Using Github / Git for version control. Commit messages should have one of the following prefixes. 

- feat: new features
- fix: bug fixes
- docs: documentation changes
- refactor: code improvements
- test: test updates
- chore: maintenance, config updates

Future plans will include CI/CD pipelines with Github Actions that use black, isort, and flake8 for code formatting. Pytest to be used for unit-testing.
