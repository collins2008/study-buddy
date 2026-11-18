Add-Type -AssemblyName System.Drawing
[Windows.Media.Ocr.OcrEngine, Windows.Foundation.Diagnostics, ContentType = WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder, Windows.Foundation.Diagnostics, ContentType = WindowsRuntime] | Out-Null
[Windows.Storage.StorageFile, Windows.Foundation.Diagnostics, ContentType = WindowsRuntime] | Out-Null

$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage([Windows.Globalization.Language]::new("en-US"))
if ($null -eq $engine) {
    $engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
}

$images = Get-ChildItem -Path "200 lvl\First Semester\SEN 201\past questions" -Include *.jpeg,*.jpg,*.png,*.webp -Recurse
$extra = Get-Item "200 lvl\First Semester\SEN 201\WhatsApp Image 2026-11-17 at 21.47.00 (1).jpeg" -ErrorAction SilentlyContinue
if ($extra) { $images += $extra }

$outFile = "app\content\SEN 201\_work\ocr_past_questions.txt"
"" | Out-File -FilePath $outFile -Encoding utf8

function Run-Ocr($filePath) {
    try {
        # Convert webp or jpeg to temp bmp/png if needed, or open directly
        $resolved = (Resolve-Path $filePath).Path
        $tempPng = [System.IO.Path]::Combine([System.IO.Path]::GetTempPath(), [System.Guid]::NewGuid().ToString() + ".png")
        
        # Use System.Drawing to convert to standard png
        $bmp = [System.Drawing.Image]::FromFile($resolved)
        $bmp.Save($tempPng, [System.Drawing.Imaging.ImageFormat]::Png)
        $bmp.Dispose()

        $asyncFile = [Windows.Storage.StorageFile]::GetFileFromPathAsync($tempPng)
        $storageFile = $asyncFile.GetAwaiter().GetResult()
        
        $asyncStream = $storageFile.OpenAsync([Windows.Storage.FileAccessMode]::Read)
        $stream = $asyncStream.GetAwaiter().GetResult()
        
        $asyncDecoder = [Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)
        $decoder = $asyncDecoder.GetAwaiter().GetResult()
        
        $asyncBitmap = $decoder.GetSoftwareBitmapAsync()
        $bitmap = $asyncBitmap.GetAwaiter().GetResult()
        
        $asyncOcr = $engine.RecognizeAsync($bitmap)
        $result = $asyncOcr.GetAwaiter().GetResult()
        
        $stream.Dispose()
        Remove-Item $tempPng -ErrorAction SilentlyContinue
        return $result.Text
    } catch {
        return "ERROR: $_"
    }
}

foreach ($img in $images) {
    Write-Host "Processing: $($img.Name)..."
    $text = Run-Ocr $img.FullName
    "=== FILE: $($img.Name) ===" | Out-File -FilePath $outFile -Append -Encoding utf8
    $text | Out-File -FilePath $outFile -Append -Encoding utf8
    "`n`n" | Out-File -FilePath $outFile -Append -Encoding utf8
}

Write-Host "Done! Saved to $outFile"
