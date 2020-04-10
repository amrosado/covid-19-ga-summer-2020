const path = require('path');
const app_root = 'src'

module.exports = {
    plugins: [
        new CleanWebpackPlugin(
            {
                cleanOnceBeforeBuildPatterns: ['dist'],
                cleanOnceAfterBuildPatterns: ['dist']
            }
        )
    ],
    entry: [
        "core-js",
        __dirname + "/" + app_root + "/index.jsx",
    ],
    module: {
        rules: [
            {
                test: /.jsx?$/,
                exclude: /(node_modules|bower_components)/,
                loader: 'babel-loader'
            },
            {
                test: /.js$/,
                exclude: /(node_modules|bower_components)/,
                loader: 'babel-loader'
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'postcss-loader']
            },
            {
                test: /\.scss$/,
                use: ['style-loader', 'postcss-loader']
            }
        ],
    },
    resolve: {
        extensions: ['.js', '.jsx']
    },
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'dist')
    }
}
