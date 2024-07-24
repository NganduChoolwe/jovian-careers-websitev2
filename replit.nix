{ pkgs }: {
  deps = [
    pkgs.inetutils
    pkgs.unixtools.ping
    pkgs.cowsay
  ];
}