import os

def batch_process_images(folder_path):
    results = {'Image Name': [], 'Percentage Damaged': []}
    
    # Iterate over each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(folder_path, filename)
            percentage_damaged = analyze_image(image_path)
            results['Image Name'].append(filename)
            results['Percentage Damaged'].append(percentage_damaged)
    
    # Convert results to a pandas DataFrame
    results_df = pd.DataFrame(results)
    
    # Export to Excel
    results_df.to_excel('image_analysis_results.xls', index=False)

# Example usage
batch_process_images('/path/to/your/images')
