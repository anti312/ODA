import os
import cv2

# Function to get a fixed color for each class
def get_class_color(class_id):
    class_colors = {
        1: (0, 255, 0),   # Class 1: Green
        2: (0, 0, 255),   # Class 2: Red
        3: (255, 255, 0), # Class 3: Yellow
        4: (0, 255, 255), # Class 4: Cyan
    }
    
    # Return the color associated with the class
    return class_colors[class_id]


# Function to process images and annotation files
def process_multiple_images(images_folder, txt_folder):
    
    for image_name in os.listdir(images_folder):
        if image_name.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(images_folder, image_name)
            txt_path = os.path.join(txt_folder, os.path.splitext(image_name)[0] + ".txt")
            
            # Draw the bounding boxes for each image
            if os.path.exists(txt_path):
                draw_bounding_boxes(image_path, txt_path)


# Function to draw bounding boxes on the image
def draw_bounding_boxes(image_path, txt_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    
    # Read the text file containing the bounding box coordinates
    with open(txt_path, 'r') as file:
        for line in file:
            
            coords = line.strip().split(',')
            class_id, x_min, y_min, x_max, y_max = int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3]), int(coords[4])

            # Get the color for the class
            color = get_class_color(class_id)

            # Draw the bounding box with the assigned color
            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, 2)

    # Display the image with the bounding boxes drawn
    cv2.namedWindow("Image with Bounding Boxes", cv2.WINDOW_NORMAL)
    cv2.imshow("Image with Bounding Boxes", image)

    # Press any key to close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Set the directories for images and annotation files
script_directory = os.path.dirname(os.path.realpath(__file__))
dataset_folder = os.path.join(script_directory, "dataset")
txt_folder = os.path.join(dataset_folder, "annotations")

# Process the images in the dataset folder
process_multiple_images(dataset_folder, txt_folder)
