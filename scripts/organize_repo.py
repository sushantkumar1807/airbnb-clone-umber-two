import os
import shutil

os.makedirs('scripts', exist_ok=True)
os.makedirs('extra', exist_ok=True)

scripts_list = [
    'analyze_dump.cjs',
    'build_app_css.cjs',
    'capture_3_views.py',
    'capture_all_previews.py',
    'capture_overlays.js',
    'capture_preview.py',
    'check_content_left.cjs',
    'check_loc.cjs',
    'check_slice_edges.cjs',
    'check_svg_tags.cjs',
    'clean_slices.cjs',
    'convert_webp.py',
    'create_submission_zip.py',
    'debug_photos.py',
    'download_nearby.py',
    'download_photos.py',
    'dump_state.py',
    'extract_chrome_cache.py',
    'extract_full_sections.cjs',
    'extract_photos.py',
    'extract_photos_map.cjs',
    'extract_real_amenities.py',
    'extract_slices.cjs',
    'find_host.py',
    'find_real_amenities.py',
    'find_svgs.py',
    'fix_jsx.cjs',
    'generate_all_components.cjs',
    'generate_arch_svg.py',
    'generate_listing_data.py',
    'generate_ui_assets.py',
    'group_imgs.cjs',
    'inspect_20_23.py',
    'inspect_imgs.cjs',
    'inspect_ref.cjs',
    'inspect_secs.py',
    'list_all_photos.py',
    'list_pt_media.py',
    'list_sections.py',
    'map_uuid_photos.py',
    'parse_airbnb.py',
    'parse_sections.cjs',
    'rebuild_safe_css.cjs',
    'sanitize_slices.cjs',
    'search_amenities.py',
    'search_similar.py',
    'test_cdp.py',
    'update_source_html.py',
]

extra_list = [
    'airbnb-clone-source (1).html',
    'airbnb_room.html',
    'airbnb_state.json',
    'clean_structure.html',
    'crop_header.png',
    'crop_house_test.png',
    'crop_searchbar.png',
    'crop_user_top.png',
    'decoded_bundle.js',
    'formatted_ref.css',
    'preview_lightbox.png',
    'preview_listing.png',
    'preview_photo_tour.png',
    'real_amenities.json',
    'ref_aheesh.png',
    'ref_aheesh_clean.png',
    'ref_discount_icon.png',
    'ref_dump.html',
    'ref_host_avatar.png',
    'ref_image1.png',
    'ref_image2.png',
    'ref_image3.png',
    'ref_photos_map.json',
    'ref_samiksha.png',
    'ref_samiksha_clean.png',
    'ref_sections',
    'ref_sleep_living_room.png',
    'ref_style_0.css',
    'test_hero.jpg',
    'test_render.png',
    'assets',
]

for item in scripts_list:
    if os.path.exists(item):
        dest = os.path.join('scripts', item)
        if os.path.exists(dest):
            if os.path.isdir(dest):
                shutil.rmtree(dest)
            else:
                os.remove(dest)
        shutil.move(item, dest)
        print(f"Moved {item} -> scripts/")

for item in extra_list:
    if os.path.exists(item):
        dest = os.path.join('extra', item)
        if os.path.exists(dest):
            if os.path.isdir(dest):
                shutil.rmtree(dest)
            else:
                os.remove(dest)
        shutil.move(item, dest)
        print(f"Moved {item} -> extra/")

print("Organization complete.")
