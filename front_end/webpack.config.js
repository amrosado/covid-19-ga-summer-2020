var app_root = "src";
var path = require("path");
var webpack = require("webpack");
var CleanWebpackPlugin = require("clean-webpack-plugin");

module.exports = {
  resolve: {
    extensions: ['.ts', '.tsx', '.js', '.jsx']
  },
  entry: [
    "webpack-dev-server/client?http://localhost:3000",
    "webpack/hot/only-dev-server",
    "core-js",
    __dirname + "/" + app_root + "/index.jsx",
  ],
  output: {
    path: __dirname + "/public/js",
    publicPath: "js/",
    filename: "bundle.js",
  },
  module: {
    rules: [
      {
        test: /(.jsx?$)|(.js$)/,
        exclude: /(node_modules|bower_components)/,
        use:{
          loader: 'babel-loader',
        }
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
  devServer: {
    contentBase: __dirname + "/public",
    host: 'localhost',
    port: 3000
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
      },
    }),
  ],
};
