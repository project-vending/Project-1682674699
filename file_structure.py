
import os

# Set root directory for machine learning project
root_dir = './ML_Project'

# Set subdirectories for different data splits
train_dir = os.path.join(root_dir, 'train')
val_dir = os.path.join(root_dir, 'validation')
test_dir = os.path.join(root_dir, 'test')

# Create root directory
os.mkdir(root_dir)

# Create subdirectories for each data split
os.mkdir(train_dir)
os.mkdir(val_dir)
os.mkdir(test_dir)

# Create empty training files
with open(os.path.join(train_dir, 'train_data_1.csv'), 'w') as f:
    pass

with open(os.path.join(train_dir, 'train_data_2.csv'), 'w') as f:
    pass

# Create empty validation files
with open(os.path.join(val_dir, 'val_data_1.csv'), 'w') as f:
    pass

with open(os.path.join(val_dir, 'val_data_2.csv'), 'w') as f:
    pass

# Create empty test files
with open(os.path.join(test_dir, 'test_data_1.csv'), 'w') as f:
    pass

with open(os.path.join(test_dir, 'test_data_2.csv'), 'w') as f:
    pass
