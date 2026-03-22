#!/bin/bash

# 1. Rename all .less files to .scss
echo "Renaming .less files to .scss..."
find . -name "*.less" -exec sh -c 'mv "$1" "${1%.less}.scss"' _ {} \;

# 2. Convert LESS variables (@var) to SCSS variables ($var)
# This handles both declarations (@color: #fff;) and usage (color: @color;)
echo "Converting variables (@ to $)..."
find . -name "*.scss" -type f -exec sed -i '' 's/@\([a-zA-Z0-9_-]\{1,\}\)/$\1/g' {} +

# 3. Fix the specific LESS 'mixin' syntax to match SCSS (basic cases)
# Note: Complex mixins might still need manual touch-ups
echo "Updating mixin syntax..."
find . -name "*.scss" -type f -exec sed -i '' 's/\. \([a-zA-Z0-9_-]\{1,\}\)(/@include \1(/g' {} +

# 4. Remove the broken plugin and gems
echo "Cleaning up legacy dependencies..."
rm -f _plugins/less-converter.rb
bundle remove less mini_racer 2>/dev/null || true

echo "------------------------------------------------"
echo "Done! Final Steps:"
echo "1. Ensure your main CSS file (e.g., css/style.scss) has '---' front matter at the top."
echo "2. Run 'bundle install' and then 'bundle exec jekyll serve'."
