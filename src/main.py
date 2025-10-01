from copy_static import copy_static_to_public

def main():
    # Generate the site by copying all of static/ into public/
    copy_static_to_public("static", "public")

if __name__ == "__main__":
    main()
