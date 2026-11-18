Add-Type -AssemblyName System.Runtime.WindowsRuntime
[Windows.Media.Ocr.OcrEngine, Windows.Foundation.Diagnostics, ContentType = WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder, Windows.Foundation.Diagnostics, ContentType = WindowsRuntime] | Out-Null
[Windows.Storage.StorageFile, Windows.Foundation.Diagnostics, ContentType = WindowsRuntime] | Out-Null

$asTask = [System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object { 
    $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' 
}

function Await-Op($op, $type) {
    $method = $asTask.MakeGenericMethod($type)
    $task = $method.Invoke($null, @($op))
    $task.Wait()
    return $task.Result
}

$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
if ($null -eq $engine) {
    Write-Error "Could not create OCR engine."
    exit 1
}

$f = Get-Item "200 lvl\First Semester\IFT 203\WhatsApp Image 2026-11-17 at 21.47.00.jpeg"
$outFile = "app\content\IFT 203\_work\ocr_notes.txt"

Write-Host "OCRing $($f.Name)..."
try {
    $storageFile = Await-Op ([Windows.Storage.StorageFile]::GetFileFromPathAsync($f.FullName)) ([Windows.Storage.StorageFile])
    $stream = Await-Op ($storageFile.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
    $decoder = Await-Op ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
    $bitmap = Await-Op ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
    $result = Await-Op ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])
    
    $stream.Dispose()

    $result.Text | Out-File -FilePath $outFile -Encoding utf8
    Write-Host "Success: $($result.Lines.Count) lines extracted."
    Write-Host $result.Text
} catch {
    Write-Host "Error OCRing $($f.Name): $_"
}
