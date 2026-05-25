%global srcname Pokemon-Terminal

Name:           pokemon-terminal
Version:        1.3.0
Release:        1%{?dist}
Summary:        Pokemon terminal themes

License:        GPLv3
URL:            https://github.com/LazoVelko/Pokemon-Terminal
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
719 unique Pokemon, from Kanto, Johto, Hoenn, Sinnoh, Unova, and Kalos.
Change the Terminal Background & Desktop Wallpaper.
Supports iTerm2, Terminology, Tilix and ConEmu.}

%description %{_description}

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
# No tests shipped in the tarball; skipping for now.

%files
%license LICENSE
%doc README.md
%{_bindir}/pokemon
%{_bindir}/ichooseyou
%{python3_sitelib}/pokemonterminal/
%{python3_sitelib}/pokemon_terminal-%{version}*.dist-info/

%changelog
* Sun May 24 2026 Your Name <support.chandrakishor@gmail.com> - 1.3.0-1
- Initial RPM package
