# Core files
node-sass --include-path node_modules assets/src/scss/app.scss assets/dist/css/app.css --output-style compressed

# Select2
node-sass --include-path node_modules assets/src/scss/components/select2/core.scss assets/dist/css/select2.css --output-style compressed
