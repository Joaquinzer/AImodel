import os
import random
import shutil

# Set the path to your original dataset folder
dataset_folder = 'D:\Documentos\Semestre8\Aplicaciones avanzadas\AI\Proyecto\AImodel\dataset'

# Set the path to the destination folder for train and test data
destination_folder = 'D:\Documentos\Semestre8\Aplicaciones avanzadas\AI\Proyecto\AImodel\images'

# Set the train-test split ratio
split_ratio = 0.8

# Create the train and test folders
train_folder = os.path.join(destination_folder, 'train')
test_folder = os.path.join(destination_folder, 'test')
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Iterate over each car brand folder in the original dataset
for brand_folder in os.listdir(dataset_folder):
    brand_folder_path = os.path.join(dataset_folder, brand_folder)
    if os.path.isdir(brand_folder_path):
        # Create the brand folder inside train and test folders
        train_brand_folder = os.path.join(train_folder, brand_folder)
        test_brand_folder = os.path.join(test_folder, brand_folder)
        os.makedirs(train_brand_folder, exist_ok=True)
        os.makedirs(test_brand_folder, exist_ok=True)

        # Get the list of images in the brand folder
        images = os.listdir(brand_folder_path)

        # Filter only JPEG files
        jpeg_images = [image for image in images if image.lower().endswith('.jpeg') or image.lower().endswith('.jpg')]

        # Shuffle the images randomly
        random.shuffle(jpeg_images)

        # Split the images into train and test sets based on the split ratio
        split_index = int(len(jpeg_images) * split_ratio)
        train_images = jpeg_images[:split_index]
        test_images = jpeg_images[split_index:]

        # Move train images to the train brand folder
        for train_image in train_images:
            src = os.path.join(brand_folder_path, train_image)
            dst = os.path.join(train_brand_folder, train_image)
            shutil.copy(src, dst)

        # Move test images to the test brand folder
        for test_image in test_images:
            src = os.path.join(brand_folder_path, test_image)
            dst = os.path.join(test_brand_folder, test_image)
            shutil.copy(src, dst)
