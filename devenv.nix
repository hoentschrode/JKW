{ pkgs, lib, config, inputs, devenv-zsh, ... }:

{
  # https://devenv.sh/basics/
  env.GREET = "devenv";

  imports = [ devenv-zsh.plugin ];
  zsh.enable = true;

  # https://devenv.sh/packages/
  packages = [ 
    pkgs.git 
  ];

  # https://devenv.sh/languages/
  languages = {
    python={
      enable = true;
      version = "3.10.12";
      venv.enable = true;
      venv.requirements = "./requirements/development.txt";
    };
  };

  enterShell = ''
    git --version
  '';

  # https://devenv.sh/tasks/
  # tasks = {
  #   "myproj:setup".exec = "mytool build";
  #   "devenv:enterShell".after = [ "myproj:setup" ];
  # };

  # https://devenv.sh/tests/
  enterTest = ''
    echo "Running tests"
    git --version | grep --color=auto "${pkgs.git.version}"
  '';

  # https://devenv.sh/git-hooks/
  # git-hooks.hooks.shellcheck.enable = true;

  # See full reference at https://devenv.sh/reference/options/
}
