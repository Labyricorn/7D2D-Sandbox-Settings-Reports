$managedPath = "g:\SteamLibrary\steamapps\common\7 Days To Die\7DaysToDie_Data\Managed"
[System.IO.Directory]::SetCurrentDirectory($managedPath)

$dlls = Get-ChildItem -Path $managedPath -Filter *.dll
foreach ($dll in $dlls) {
    try {
        [System.Reflection.Assembly]::LoadFrom($dll.FullName) > $null
    } catch {}
}

$assembly = [System.Reflection.Assembly]::LoadFrom((Join-Path $managedPath "Assembly-CSharp.dll"))
$types = @()
try {
    $types = $assembly.GetTypes()
} catch [System.Reflection.ReflectionTypeLoadException] {
    $types = $_.Exception.Types | Where-Object { $_ -ne $null }
}

$mgrType = $types | Where-Object { $_.FullName -eq "SandboxOptions.SandboxOptionManager" }
$method = $mgrType.GetMethod("LoadInternalPresets", [System.Reflection.BindingFlags]::Public -bor [System.Reflection.BindingFlags]::NonPublic -bor [System.Reflection.BindingFlags]::Instance)

if ($method -eq $null) {
    Write-Output "LoadInternalPresets method not found."
    exit
}

$body = $method.GetMethodBody()
$il = $body.GetILAsByteArray()
$module = $mgrType.Module

Write-Output "Parsing IL for LoadInternalPresets(). Length: $($il.Length)"

$i = 0
while ($i -lt $il.Length) {
    $offset = $i
    $op = $il[$i]
    $i++
    
    if ($op -eq 0xfe) {
        if ($i -ge $il.Length) { break }
        $i++
        continue
    }
    
    if ($op -eq 0x72) { # ldstr
        $token = [System.BitConverter]::ToInt32($il, $i)
        $i += 4
        try {
            $str = $module.ResolveString($token)
            Write-Output "$($offset): ldstr '$str'"
        } catch {}
    }
    elseif ($op -eq 0x28 -or $op -eq 0x6f -or $op -eq 0x73) { # call/newobj
        $token = [System.BitConverter]::ToInt32($il, $i)
        $i += 4
        try {
            $member = $module.ResolveMember($token)
            Write-Output "$($offset): call/newobj $($member.DeclaringType.FullName)::$($member.Name)"
        } catch {}
    }
}
