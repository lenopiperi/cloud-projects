import os
import sys
from shutil import copyfile
import logging

logging.basicConfig(filename='manipute-userPhoto.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logging.debug('manipute-userPhoto called')

newFilename = sys.argv[1]
updatedFilename = 'updated-' + newFilename
logging.debug('newFilename = '+ newFilename)
logging.debug('newFilename = '+ updatedFilename)

source = './uploads/' + newFilename
target = './mod-images/' + updatedFilename
logging.debug('source = '+ source)
logging.debug('target = '+ target)


try:
    copyfile(source, target)
except IOError as e:
    logging.error("Unable to copy file. %s" % e)
    logging.debug('manipute-userPhoto complete')
    sys.exit()
except:
    logging.exception('')
    logging.debug('manipute-userPhoto complete')
    sys.exit()


dataToSendBack = target

print(dataToSendBack)
sys.stdout.flush()
logging.debug('manipute-userPhoto complete')