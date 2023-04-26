/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  async rewrites() {
    return [
      {
        source: "/:path*",
        destination: `http://${process.env.API_HOST}/:path*`,
      },
    ];
  },
}

module.exports = nextConfig
