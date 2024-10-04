# Place an object’s image in a text-conditioned scene

## Introduction
This project aims to generate realistic images by seamlessly incorporating an object from an existing image into a background scene defined by a text prompt. The primary goal is to place the object naturally in a generated scene.

 The objective is to create an AI-powered image generation system that allows users to input an object (e.g., product image with a white background) and a descriptive text prompt (e.g., "toaster in a kitchen"), and generate an image where the object is realistically placed in the described background.

## Results

### Examples
#### Input Image
![image](https://github.com/user-attachments/assets/5d9d776b-3689-42e2-916f-8cfd3d059f2e)
#### CMD
PS C:\Users\rinsh\OneDrive\Desktop\Avataar> python stable.py --image C:/Users/rinsh/OneDrive/Desktop/avataar/example4.jpg --text-prompt "A chair with desk in office" --output C:/Users/rinsh/OneDrive/Desktop/avataar/generated.png
#### Output Image
![image](https://github.com/user-attachments/assets/3a202418-4948-42c0-b42a-6553d383766a)

#### Input Image 
![image](https://github.com/user-attachments/assets/75eebcd2-6dff-436d-81cc-443afac89e70)
#### CMD 
PS C:\Users\rinsh\OneDrive\Desktop\Avataar> python stable.py --image C:/Users/rinsh/OneDrive/Desktop/avataar/example5.jpg --text-prompt "A tent and a camp fire" --output C:/Users/rinsh/OneDrive/Desktop/avataar/generated6.png 
#### Output Image
![image](https://github.com/user-attachments/assets/5ba4182f-98c1-4286-9481-87ab42c20872)

#### Input Image
![image](https://github.com/user-attachments/assets/93341378-7e61-4ce4-aa36-0054f69f3f6f)
#### CMD
PS C:\Users\rinsh\OneDrive\Desktop\Avataar> python stable.py --image C:/Users/rinsh/OneDrive/Desktop/avataar/astronaut1.jpg --text-prompt "An astronaut floating in space with stars, planets, and moons." --output C:/Users/rinsh/OneDrive/Desktop/avataar/generated4.png
#### Output Image
![image](https://github.com/user-attachments/assets/ff653ff0-edbc-4a89-af65-8414392db52e)
#### Trying a Different prompt
PS C:\Users\rinsh\OneDrive\Desktop\Avataar> python stable.py --image C:/Users/rinsh/OneDrive/Desktop/avataar/astronaut1.jpg --text-prompt "object in  space ship" --output C:/Users/rinsh/OneDrive/Desktop/avataar/generated2.png
![image](https://github.com/user-attachments/assets/7cf66c11-f257-4e96-affa-943b48e3000a)

## Challenges
1. Difficulty in Adjusting Prompts: The model's output is highly sensitive to the input prompt, requiring careful tuning to get the desired combination of the object and background. Slight changes in wording can lead to vastly different results.

2. Generation of Unrealistic Images: There are instances where the generated images do not maintain realism. This can include poor blending of the provided object with the background or unnatural proportions.

3. Model Drawing its Own Pictures: Sometimes, instead of using the provided object image, the model generates its own interpretation of the object, ignoring the uploaded image entirely. This leads to inconsistency and deviates from the intended results.

4. Overfitting the Object: There are cases where the object takes up too much space in the generated image, leaving insufficient room for the background, thus affecting the overall composition.






