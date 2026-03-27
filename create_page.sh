#!/bin/bash

# -----------------------------
# Interactive Page Object Creator
# -----------------------------

echo "Enter Page Object name (e.g., DashboardPage): "
read PAGE_NAME

# Convert to snake_case for filename
FILE_NAME=$(echo "$PAGE_NAME" | sed -r 's/([A-Z])/_\1/g' | sed 's/^_//' | tr '[:upper:]' '[:lower:]')
FILE_PATH="./pages/${FILE_NAME}.py"

# Test file name
TEST_NAME="test_${FILE_NAME}.py"
TEST_PATH="./tests/${TEST_NAME}"

# -----------------------------
# Create Page Object
# -----------------------------
echo "Creating Page Object: $FILE_PATH"

cat << EOF > $FILE_PATH
from pages.base_page import BasePage

class ${PAGE_NAME}(BasePage):

    def is_loaded(self):
        # TODO: Replace with real locator
        return True
EOF

# -----------------------------
# Update PageFactory
# -----------------------------
FACTORY="./factory/page_factory.py"

echo "Updating PageFactory..."

# Insert new property before last line
sed -i '' "/class PageFactory/a\\
\\
    @property\\
    def ${FILE_NAME%.*}(self):\\
        from pages.${FILE_NAME} import ${PAGE_NAME}\\
        return ${PAGE_NAME}(self.page)\\
" $FACTORY

# -----------------------------
# Create Skeleton Test
# -----------------------------
echo "Creating test: $TEST_PATH"

cat << EOF > $TEST_PATH
from factory.page_factory import PageFactory

def test_${FILE_NAME}_loads(page):
    app = PageFactory(page)

    # TODO: Add navigation step
    assert app.${FILE_NAME%.*}.is_loaded()
EOF

echo "Done! Created:"
echo " - Page Object: $FILE_PATH"
echo " - Factory entry added to: $FACTORY"
echo " - Test: $TEST_PATH"