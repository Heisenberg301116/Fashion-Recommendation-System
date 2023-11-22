Store your custom dataset in the path: 'images/'. 

To perform inference using the model, write the test cases in 'images/test_pairs.txt' file. The file has 3 columns:

1) Column 1 represents the profile image of the person upon whom you want to fit the outfit. The image is located in 'images/humans' path.

2) Column 2 represents the outfit image name that you want to fit over this person. Depending upon the choice, you can fit a dress upon the person, a lower body outfit or an upper body outfit.

3) Column 3 can occupy values ranging from 0 to 2. '0' represents that you want to fit the outfit at the upper half of the person, '1' represents at the lower half and '2' represents that you want to fit a dress upon the whole body of the person. 