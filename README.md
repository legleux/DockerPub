## TODO
Don't using my personal machine as the runner
Build more images:
- Clio
- Sidechains
- Arbitrary repos/branches

1. Remove detritus, fix terrible names, remove hard-coded stuff
2. Build arbitrary repo/branch/commit
3. Cleaner multi-stage build
    - build deps
    - conan pkgs (`.conan/data`)
    - only rippled
4. Fix python version to 3.11.4


   {% warning %}

      If you are using a Microsoft Visual C++ compiler,
      then you will need to ensure consistency between the `build_type` setting
      and the `compiler.runtime` setting.
      When `build_type` is `Release`, `compiler.runtime` should be `MT`.
      When `build_type` is `Debug`, `compiler.runtime` should be `MTd`.

      ```
      conan install .. --output-folder . --build missing --settings build_type=Release --settings compiler.runtime=MT
      conan install .. --output-folder . --build missing --settings build_type=Debug --settings compiler.runtime=MTd
      ```


   > [!IMPORTANT]

      If you are using a Microsoft Visual C++ compiler,
      then you will need to ensure consistency between the `build_type` setting
      and the `compiler.runtime` setting.
      When `build_type` is `Release`, `compiler.runtime` should be `MT`.
      When `build_type` is `Debug`, `compiler.runtime` should be `MTd`.

      ```
      conan install .. --output-folder . --build missing --settings build_type=Release --settings compiler.runtime=MT
      conan install .. --output-folder . --build missing --settings build_type=Debug --settings compiler.runtime=MTd
      ```


   > [!INFO]

      If you are using a Microsoft Visual C++ compiler,
      then you will need to ensure consistency between the `build_type` setting
      and the `compiler.runtime` setting.
      When `build_type` is `Release`, `compiler.runtime` should be `MT`.
      When `build_type` is `Debug`, `compiler.runtime` should be `MTd`.

      ```
      conan install .. --output-folder . --build missing --settings build_type=Release --settings compiler.runtime=MT
      conan install .. --output-folder . --build missing --settings build_type=Debug --settings compiler.runtime=MTd
      ```

   > [!WARNING]

      If you are using a Microsoft Visual C++ compiler,
      then you will need to ensure consistency between the `build_type` setting
      and the `compiler.runtime` setting.
      When `build_type` is `Release`, `compiler.runtime` should be `MT`.
      When `build_type` is `Debug`, `compiler.runtime` should be `MTd`.

      ```
      conan install .. --output-folder . --build missing --settings build_type=Release --settings compiler.runtime=MT
      conan install .. --output-folder . --build missing --settings build_type=Debug --settings compiler.runtime=MTd
      ```
