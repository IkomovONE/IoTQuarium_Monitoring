const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: "/",
  devServer: {
    allowedHosts: [
      'iotquarium.info',  // Allow requests from this domain
    ],
    
    host: '0.0.0.0', // Bind to all interfaces
    port: 8080,
  },
})
