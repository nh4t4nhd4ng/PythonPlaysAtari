# PythonPlaysAtari

This project contains the source code to a deep reinforcement learning architecture written
in Python and based off [DQN 3.0](http://arxiv.org/pdf/1312.5602.pdf). It also comes with
several example Atari Roms (Missile Command, Pong, and Breakout).

## Setup Script
To run the scripts [ALE]() must first be installed. This can be done using the following commands below before
final setup is done using the python setup script.

'''bash
# Install ALE

# Install Python Dependencies
sudo python setup.py install
'''

## Usage Script

Their are three main scripts, `train.py`, `analyse.py`, and `watch.py`. To conduct the training script the requested rom must be present in the 
rom directory. To train using that game then the game name, without extension, should be passed. Help on possible arguments is available by 
parsing the help argument as is show below.

```python
#Display Roms
cd ~/roms && ls && cd ../
#Learn Pong
python train.py pong
#Help!
python train.py --help
```
To analyse the result of one of these training sessions then simply call the analysis script in the following fashion. This will provide
information on the learning rate, scoring, ect. Once again, help on possible arguments is available by parsing the help argument.

```python
python analyse.py ~/data/pong_19-03-2015
```

Finally, to visually see how well one of these games performed then it is possible to directly specify which epoch of learning you wish to 
use. If no epoch is specified then the last epoch is rendered.

```python
#Play using specific network
python watch.py ~/data/pong_19-03-2015/epoch_1.pkl
#Play using the best network
python watch.py ~/data/pong_19-03-2015
#Display argparse options
python watch.py --help
```

