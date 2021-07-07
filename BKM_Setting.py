import os
import sys
import pandas as pd
import shutil
import subprocess
import re
import glob
import numpy as np
from PyQt4.QtGui import QFileDialog
from bkmGui import *
from os import path



sys.path.insert(0, "/prj/opc/all/users/singhs6/pycharmproject/OPCPackageDelivery/")
from opcPackageCommonLib import *
fileOfChecks="/prj/opc/all/users/sangeets/sangeeta/BKMChecks.dat"
PRJOPCSOURCEDIR = os.getenv('OPCSOURCEDIR')


sys.path.insert(0, "{}/RETToolsBox/Modules/RET/ThresholdEditor/".format(PRJOPCSOURCEDIR))
from commonLib import getTechLayAbrFromDir




