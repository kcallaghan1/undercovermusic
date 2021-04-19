# undercovermusic

[Agent definition document](https://docs.google.com/document/d/1YfatTyF1Ui6guxlBx6pBeKooGJN84Sf_J7s8BFprLtY/edit?usp=sharing)

[Zenhub Link](https://app.zenhub.com/workspaces/undercovermusic-60745e6b8c0c700013c209c3/board?repos=355955144)

### Chord Progression Database
https://docs.google.com/spreadsheets/d/1SHB_B4du3JVB1kvVBUEHTpZjpqHBmugWnQVnm2stGCs/edit?usp=sharing
#### Classical Music Kaggle Download
https://www.kaggle.com/soumikrakshit/classical-music-midi

#### Instructions on how to set up/run the unit tests of the environment

#### Instructions on how a human can act as an agent
* Step1: The human agent would enter what they want to do:
  * a. Create Chord Progression b. Choose Pre-made Chord Progression c. Random Chord Progression d. Quit
* Step2 a: if the user chooses to create chord progression then he/she will be asked what type of chord progression they want to create:
  * a. Minor b. Major c. Random
   * Step2 a i: if the user chooses minor chord progression then he/she will be provided with a list of minor chord pregressions to choose from.
   * Step2 a ii: The user then chooses a minor chord, after which the user gets a minor chord progression in the form of text file, which they can play using the [Online Sequencer](https://onlinesequencer.net).
* Step2 b: if the user chose the Pre-made Chord Progression then he/she will be asked what type of pre-chord progression they want to alter:
  * a. Minor b. Major c. Random
   * Step2 b i: if the user chooses major chord progression then he/she will be provided with a list of major chord pregressions to choose from.
   * Step2 b ii: The user then chooses a major chord, after which the user gets a minor chord progression in the form of text file, which they can play using the [Online Sequencer](https://onlinesequencer.net).
* Step2 c: if the user chooses random Chord Progression then he/she will be provided with a random chord pregression that can be either major or minor, which they can play using the [Online Sequencer](https://onlinesequencer.net).
* Step3: if the user chooses to quit, the music maker will terminate.

#### Look up table analysis
* Step4: After the user creates/alters a text file he/she can use how good music has been made my our agent and compare it to the [older version](https://github.com/timothymarotta/aimusicmaker) of this project, which was created using Java.
* Step5: We will use the lookup table ... 

#### Notes to clarify where the sensor and actuator interfaces are located in the codebase

### Actuators:
Can modify or generate/write new text files (minor/major/random) that can be played via [Online Sequencer](https://onlinesequencer.net).
Present in the UI
### Sensors:
Can “read” text files (minor/major/random) that can be played on [Online Sequencer](https://onlinesequencer.net).
Present in the UI

Music AI Agents for CS354
