var path = require("path");
var webpack = require("webpack");
var BundleTracker = require("webpack-bundle-tracker");
var ip = 'localhost';

module.exports = {
    devtool: "cheap-module-eval-source-map",
    context: __dirname,

    entry: {
        mybookings: [
            "webpack-dev-server/client?http://" + ip + ":3001",
            //"webpack/hot/only-dev-server",
            "./app",
        ],
        common: ['react'],

    },

    output: {

        path: path.resolve('../static/bundles/'),
        publicPath: "http://" + ip + ":3001/static/bundles/",
        filename: "[name].[hash].js",
        chunkFilename: "[id].[hash].js",
        library: "[name]",
        // filename: "[name]-[hash].js",
    },

    plugins: [
        // new webpack.optimize.CommonsChunkPlugin('vendors', 'vendors.js'),
        new webpack.optimize.CommonsChunkPlugin({
         name: 'common',
        }),
        new webpack.optimize.CommonsChunkPlugin({
            children: true,
            async: true,
        }),
        new webpack.optimize.DedupePlugin(),
        new webpack.optimize.UglifyJsPlugin({
            beautify: false,
            comments: false,
            compress: {
                sequences: true,
                booleans: true,
                loops: true,
                unused: true,
                warnings: false,
                drop_console: true,
                unsafe: true
            }
        }),
        new webpack.optimize.OccurrenceOrderPlugin(),
        new webpack.NoErrorsPlugin(), // don't reload if there is an error
        new webpack.HotModuleReplacementPlugin(),
        new BundleTracker({filename: "./webpack-stats.json"})

    ],


    resolve: {
        modulesDirectories: ["node_modules"],
        extensions: ["", ".js", ".jsx"]
    },

    resolveLoader: {
        modulesDirectories: ["node_modules"],
        moduleTemplates: ["*-loader", "*"],
        extensions: ["", ".js", ".jsx"]
    },

    module: {
        loaders: [
            {
                test: /\.(json)$/,
                exclude: /node_modules/,
                loader: 'json',
            },
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                loader: 'babel',
                query: {
                    plugins: [
                        'transform-runtime',
                        'transform-react-remove-prop-types',
                        'transform-react-constant-elements',
                        'transform-react-inline-elements'
                    ],
                    presets: ['es2015', 'stage-0', 'react']
                }
            },
            {
                test: /\.css$/,
                loader: 'style!css?autoprefixer?browsers=last 2 versions',
                // loader: 'style!css?modules=true&localIdentName=[name]-[local]-[hash:base64:5]',
            },
            {
                test: /\.less$/,
                loader: 'style!css?autoprefixer?browsers=last 2 versions!less',
                // loader: 'style!css?modules=true&localIdentName=[name]-[local]-[hash:base64:5]!less',
            },
            {
                test: /\.(?:png|jpg|gif|svg|ttf|eot|woff|woff2)$/,
                loader: 'file?name=[path][name].[ext]'
            },
        ]
    },


};