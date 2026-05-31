// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "AkilliSporcu",
    platforms: [
        .iOS(.v16)
    ],
    products: [
        .library(
            name: "AkilliSporcu",
            targets: ["AkilliSporcu"]
        )
    ],
    dependencies: [],
    targets: [
        .target(
            name: "AkilliSporcu",
            path: "Sources"
        )
    ]
)
