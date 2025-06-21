package org.example.backend;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
public class BoardController {

    private final PostRepository postRepository;

    public BoardController(PostRepository postRepository) {
        this.postRepository = postRepository;
    }

    @GetMapping("/")
    public String index(Model model) {
        List<Post> posts = postRepository.findAll();
        model.addAttribute("posts", posts);
        return "index";
    }

    @GetMapping("/write")
    public String writeForm(Model model) {
        model.addAttribute("post", new Post());
        return "write";
    }

    @PostMapping("/write")
    public String submitPost(@ModelAttribute Post post) {
        postRepository.save(post);
        return "redirect:/";
    }
}
