import './Header.css';

function Header() {
  return (
    <header className="header">
    <a href="/">
      <img
        className="header-logo"
        src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg"
        alt="Netflix Logo"
      />
    </a>
      <img
        className="header-avatar"
        src="https://upload.wikimedia.org/wikipedia/commons/0/0b/Netflix-avatar.png"
        alt="User Avatar"
      />
    </header>
  );
}

export default Header;
