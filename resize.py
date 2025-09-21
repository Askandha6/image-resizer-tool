def batch_resize_convert(input_folder, output_folder, size=(800, 600), output_format="JPEG"):
    """
    Resize and convert images in batch.
    
    :param input_folder: Path to input folder containing images
    :param output_folder: Path to save resized/converted images
    :param size: Tuple (width, height) for resizing
    :param output_format: Output image format (e.g., "JPEG", "PNG", "WEBP")
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        try:
            with Image.open(file_path) as img:
                img_resized = img.resize(size, Image.Resampling.LANCZOS)

                base_name = os.path.splitext(filename)[0]
                new_filename = f"{base_name}.{output_format.lower()}"

                save_path = os.path.join(output_folder, new_filename)
                img_resized.save(save_path, output_format)

                print(f"Processed: {filename} -> {new_filename}")
        except Exception as e:
            print(f"Skipping {filename}: {e}")
