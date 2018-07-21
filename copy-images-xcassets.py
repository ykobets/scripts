#
#   Script for copying images through all xcassets in Xcode
#   Add one PNG image to xcasset file to 1X - in the highest quality
#   And this image will be used for all resolutions 1X, 2X, 3X   
#

import os, json, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', help='Images xcassets folder')
args = parser.parse_args()

filenames = os.listdir(args.path)

result = []

for dir_name in filenames:
        if os.path.isdir(os.path.join(args.path, dir_name)):
            result.append(dir_name)
            
            path = os.path.join(args.path, dir_name) + '/Contents.json'

            if os.path.exists(path) and os.stat(path).st_size > 0:
                with open(path, 'r+', encoding='utf-8') as data_file:
                    
                    data = json.loads(data_file.read())
                    filename = None
                    if 'images' in data:
                        for img in data['images']: 
                            if 'filename' in img:
                                filename = img['filename']


                    if filename is not None:
                        for img in data['images']:
                            img['filename'] = filename
                            result.append(path)

                    data_file.seek(0)
                    data_file.truncate()
                    json.dump(data, data_file)
                    data_file.close()                    

result.sort()

print('*** Completed. Script modified ' + str(len(result)) + ' files.')

