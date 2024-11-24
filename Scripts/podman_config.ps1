# podman_config.ps1

# Check if Podman is installed
$podmanPath = "C:\Program Files\RedHat\Podman"
if (!(Test-Path $podmanPath)) {
    Write-Host "Podman is not installed at $podmanPath"
    exit
}

# Add Podman to the PATH
$env:PATH = "$podmanPath;$env:PATH"

Write-Host "Podman added to PATH successfully!"
