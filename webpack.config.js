var path = require('path');

module.exports = {
    entry: {
        app: path.join(__dirname, "/assets/src/js/app.js"),
    },
    output: {
        path: path.join(__dirname, "assets/dist/js"),
        filename: "[name].js"
    },
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
                query: {
                    presets: ['react', 'es2015', 'stage-2']
                }
            },
            {
                test: /\.scss$/,
                loader: 'style!css!sass!sass-resources'
            },
            {
                test: /bootstrap\/dist\/js\/umd\//,
                loader: 'imports?jQuery=jquery'
            },
            {test: /\.(woff2?|svg)$/, loader: 'url?limit=10000'},
            {test: /\.(ttf|eot)$/, loader: 'file'}
        ]
    },
    resolve: {
        extensions: ['.js', '.jsx']
    }
};
