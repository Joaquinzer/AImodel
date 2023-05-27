import os
import random
import shutil

dataset_folder = 'D:\Documentos\Semestre8\Aplicaciones avanzadas\AI\Proyecto\AImodel\dataset'
# Set the path to the destination folder for train, validation, and test data
destination_folder = 'D:\Documentos\Semestre8\Aplicaciones avanzadas\AI\Proyecto\AImodel\images'

# Set the train-validation-test split ratios
train_ratio = 0.6
validation_ratio = 0.2
test_ratio = 0.2

# Create the train, validation, and test folders
train_folder = os.path.join(destination_folder, 'train')
validation_folder = os.path.join(destination_folder, 'validation')
test_folder = os.path.join(destination_folder, 'test')
os.makedirs(train_folder, exist_ok=True)
os.makedirs(validation_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Iterate over each car brand folder in the original dataset
for brand_folder in os.listdir(dataset_folder):
    brand_folder_path = os.path.join(dataset_folder, brand_folder)
    if os.path.isdir(brand_folder_path):
        # Create the brand folder inside train, validation, and test folders
        train_brand_folder = os.path.join(train_folder, brand_folder)
        validation_brand_folder = os.path.join(validation_folder, brand_folder)
        test_brand_folder = os.path.join(test_folder, brand_folder)
        os.makedirs(train_brand_folder, exist_ok=True)
        os.makedirs(validation_brand_folder, exist_ok=True)
        os.makedirs(test_brand_folder, exist_ok=True)

        # Get the list of images in the brand folder
        images = os.listdir(brand_folder_path)

        # Filter only JPEG files
        jpeg_images = [image for image in images if image.lower().endswith('.jpeg') or image.lower().endswith('.jpg')]

        # Shuffle the images randomly
        random.shuffle(jpeg_images)

        # Split the images into train, validation, and test sets based on the split ratios
        train_index = int(len(jpeg_images) * train_ratio)
        validation_index = int(len(jpeg_images) * (train_ratio + validation_ratio))
        train_images = jpeg_images[:train_index]
        validation_images = jpeg_images[train_index:validation_index]
        test_images = jpeg_images[validation_index:]

        # Move train images to the train brand folder
        for train_image in train_images:
            src = os.path.join(brand_folder_path, train_image)
            dst = os.path.join(train_brand_folder, train_image)
            shutil.copy(src, dst)

        # Move validation images to the validation brand folder
        for validation_image in validation_images:
            src = os.path.join(brand_folder_path, validation_image)
            dst = os.path.join(validation_brand_folder, validation_image)
            shutil.copy(src, dst)

        # Move test images to the test brand folder
        for test_image in test_images:
            src = os.path.join(brand_folder_path, test_image)
            dst = os.path.join(test_brand_folder, test_image)
            shutil.copy(src, dst)

