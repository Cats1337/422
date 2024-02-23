{ pkgs }: {
    deps = [
      pkgs.gradle
      pkgs.apacheAnt_1_9
        pkgs.graalvm17-ce
        pkgs.maven
        pkgs.replitPackages.jdt-language-server
        pkgs.replitPackages.java-debug
    ];
}